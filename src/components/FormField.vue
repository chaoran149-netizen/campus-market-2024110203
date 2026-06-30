<script setup lang="ts">
defineProps<{
  label: string
  error?: string
  required?: boolean
}>()
</script>

<template>
  <div class="form-field">
    <label class="form-label">
      {{ label }}
      <span v-if="required" class="required-mark">*</span>
    </label>
    <slot />
    <p v-if="error" class="form-error">{{ error }}</p>
  </div>
</template>

<style scoped>
.form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--color-text);
}

.required-mark {
  color: #DC2626;
  font-weight: 700;
}

.form-error {
  font-size: 12px;
  color: #DC2626;
}
</style>
