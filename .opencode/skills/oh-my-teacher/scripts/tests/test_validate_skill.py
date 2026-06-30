"""Tests for scripts/validate_skill.py."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from validate_skill import (  # noqa: E402
    ALLOWED_CAPABILITY_TAGS,
    ALLOWED_OPTIMIZATION_PROFILES,
    DANGEROUS_REASONING_PATTERNS,
    GRADE_OUTPUT_SECTIONS,
    IMA_SKILLS,
    IMA_TOOLS,
    REQUIRED_AGENT_IDS,
    commands_from_index,
    course_template_keys,
    find_mojibake,
    frontmatter,
    index_primary_map,
    load_agent_registry,
    skill_quick_map,
)


class ValidateSkillTests(unittest.TestCase):
    def test_skill_frontmatter_has_required_keys(self):
        text = (ROOT_DIR / "SKILL.md").read_text(encoding="utf-8")
        fm_keys = set(frontmatter(text))
        self.assertTrue(fm_keys >= {"name", "description"}, f"Missing required keys: {fm_keys}")
        self.assertFalse(fm_keys - {"name", "description"})

    def test_index_includes_core_and_ima_commands(self):
        text = (ROOT_DIR / "references" / "INDEX.md").read_text(encoding="utf-8")
        commands = commands_from_index(text)
        for command in [
            "/help",
            "/profile",
            "/materials",
            "/paper",
            "/lab",
            "/diagnose",
            "/plan",
            "/map",
            "/explain",
            "/socratic",
            "/feynman",
            "/quiz",
            "/mock",
            "/oral",
            "/grade",
            "/fix",
            "/flashcards",
            "/review-due",
            "/group-quiz",
            "/visual",
            "/video",
            "/code-demo",
            "/cram",
            "/resume",
            "/summary",
            "/mode",
            "/source-map",
            "/paper-analyze",
            "/teacher-emphasis",
            "/wrong-note",
            "/dashboard",
            "/last-page",
            "/report",
            "/ppt",
        ]:
            self.assertIn(command, commands)

    def test_ima_adapter_mentions_all_native_tools_and_skills(self):
        text = (ROOT_DIR / "references" / "ima-adaptation.md").read_text(encoding="utf-8")
        for tool in IMA_TOOLS:
            self.assertIn(tool, text)
        for skill in IMA_SKILLS:
            self.assertIn(skill, text)
        self.assertIn("only when shell is explicitly available", text)

    def test_chinese_routing_covers_common_triggers(self):
        text = (ROOT_DIR / "references" / "chinese-routing.md").read_text(encoding="utf-8")
        for phrase in ["老师说这些是重点", "帮我看往年题怎么复习", "整理错题", "今天该复习什么", "生成复习 PPT"]:
            self.assertIn(phrase, text)

    def test_ima_agent_exists(self):
        text = (ROOT_DIR / "agents" / "ima.yaml").read_text(encoding="utf-8")
        for phrase in ["SKILL.md", "ima-native", "search source=kb", "ima-note", "task_plan"]:
            self.assertIn(phrase, text)

    def test_environment_reference_exists(self):
        text = (ROOT_DIR / "references" / "environment-adaptation.md").read_text(encoding="utf-8")
        for phrase in ["agent-shell", "rag-notebook", "notes-app", "plain-chat", "ima-native"]:
            self.assertIn(phrase, text)

    def test_mode_protocol_references_exist(self):
        socratic = (ROOT_DIR / "references" / "socratic-mode.md").read_text(encoding="utf-8")
        feynman = (ROOT_DIR / "references" / "feynman-mode.md").read_text(encoding="utf-8")
        self.assertIn("Hint ladder", socratic)
        self.assertIn("Teacher close", socratic)
        self.assertIn("Feynman Check", feynman)
        self.assertIn("Repair Card", feynman)

    def test_examples_cover_signature_modes_and_ima(self):
        text = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT_DIR / "examples").glob("*.md"))
        self.assertIn("/socratic", text)
        self.assertIn("/feynman", text)
        self.assertIn("ima", text.lower())

    def test_examples_contain_full_grade_contract(self):
        text = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT_DIR / "examples").glob("*.md"))
        self.assertIn("/grade", text)
        for section in GRADE_OUTPUT_SECTIONS:
            self.assertIn(section, text, f"golden /grade example missing {section}")

    def test_dangerous_reasoning_patterns_do_not_include_empty_string(self):
        self.assertNotIn("", DANGEROUS_REASONING_PATTERNS)

    def test_agent_configs_do_not_request_hidden_reasoning_or_mojibake(self):
        text = "\n".join(path.read_text(encoding="utf-8").lower() for path in (ROOT_DIR / "agents").glob("*.*"))
        self.assertNotIn("write your reasoning chain", text)
        self.assertNotIn("chain-of-thought", text)
        self.assertNotIn("<thought>", text)
        self.assertNotIn("????", text)

    def test_common_course_templates_exist(self):
        templates = course_template_keys(ROOT_DIR / "scripts" / "course_templates.py")
        for template in [
            "advanced-math",
            "physics",
            "programming-c-cpp",
            "digital-logic",
            "marxism-basic-principles",
        ]:
            self.assertIn(template, templates)

    def test_agent_registry_covers_required_agents(self):
        registry = load_agent_registry(ROOT_DIR)
        ids = {entry["id"] for entry in registry["agents"]}
        self.assertTrue(REQUIRED_AGENT_IDS <= ids)
        self.assertIn(registry["default_agent"], ids)

    def test_agent_registry_adapters_and_inventory_are_consistent(self):
        registry = load_agent_registry(ROOT_DIR)
        inventory = (ROOT_DIR / "references" / "agent-inventory.md").read_text(encoding="utf-8")
        for entry in registry["agents"]:
            agent_id = entry["id"]
            adapter = ROOT_DIR / entry["adapter_path"]
            self.assertTrue(adapter.exists(), f"Missing adapter for {agent_id}")
            text = adapter.read_text(encoding="utf-8")
            self.assertIn("SKILL.md", text)
            self.assertIn("agent-adapter-contract.md", text)
            self.assertIn("agent-optimization.md", text)
            self.assertIn("agent-inventory.md", text)
            self.assertIn("Best path:", text)
            self.assertIn(f'agent_id: "{agent_id}"', text)
            self.assertIn(f"### {agent_id}", inventory)
            self.assertTrue(set(entry["capability_tags"]) <= ALLOWED_CAPABILITY_TAGS)
            self.assertTrue(set(entry["optimization_profiles"]) <= ALLOWED_OPTIMIZATION_PROFILES)
            self.assertTrue(entry["optimization_profiles"], f"Missing optimization profile for {agent_id}")

    def test_reminder_capabilities_are_supported_by_validator(self):
        self.assertIn("proactive-message", ALLOWED_CAPABILITY_TAGS)
        self.assertIn("scheduler", ALLOWED_CAPABILITY_TAGS)
        self.assertIn("reminder-agent", ALLOWED_OPTIMIZATION_PROFILES)

    def test_skill_quick_map_matches_index_primary(self):
        quick = skill_quick_map((ROOT_DIR / "SKILL.md").read_text(encoding="utf-8"))
        primary = index_primary_map((ROOT_DIR / "references" / "INDEX.md").read_text(encoding="utf-8"))
        known_refs = {p.name for p in (ROOT_DIR / "references").glob("*.md")}
        self.assertGreater(len(quick), 20, "quick routing map failed to parse")
        # Split row must be paired positionally, not cross-producted.
        self.assertEqual(quick.get("/socratic"), "socratic-mode.md")
        self.assertEqual(quick.get("/feynman"), "feynman-mode.md")
        for command, skill_ref in quick.items():
            idx_ref = primary.get(command)
            self.assertIsNotNone(idx_ref, f"{command} in quick map but not in INDEX catalog")
            if idx_ref in known_refs:
                self.assertEqual(skill_ref, idx_ref, f"routing drift for {command}")

    def test_routing_drift_is_detectable(self):
        skill = (
            "Quick routing map\n"
            "| Primary reference | Commands |\n"
            "|---|---|\n"
            "| `wrong-ref.md` | `/explain` |\n"
            "\nNext section\n"
        )
        index = (
            "## Command Catalog\n"
            "| Command | Description | Primary Reference | Secondary |\n"
            "|---|---|---|---|\n"
            "| `/explain` | x | `subject-adaptation.md` | - |\n"
            "## Next\n"
        )
        self.assertEqual(skill_quick_map(skill).get("/explain"), "wrong-ref.md")
        self.assertEqual(index_primary_map(index).get("/explain"), "subject-adaptation.md")

    def test_find_mojibake_flags_replacement_char_and_question_run(self):
        self.assertTrue(find_mojibake("正常�文本"))
        self.assertTrue(find_mojibake("see ???? here"))
        self.assertEqual(find_mojibake("正常的中文 and English"), [])

    def test_cli_passes_for_repo(self):
        script = SCRIPT_DIR / "validate_skill.py"
        for path in ROOT_DIR.rglob("__pycache__"):
            if path.is_dir():
                shutil.rmtree(path)
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        result = subprocess.run(
            [sys.executable, str(script), "--root", str(ROOT_DIR)],
            capture_output=True,
            text=True,
            cwd=str(ROOT_DIR),
            env=env,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Skill validation passed.", result.stdout)


if __name__ == "__main__":
    unittest.main()
