<template>
  <div
    class="inline gap-x-8 gap-y-4 px-9 py-1.5 rounded-lg select-none capitalize truncate"
    :class="
      status != 'kasutaja'
        ? 'text-white/90 bg-blue-600/80'
        : 'text-gray-400/90 bg-blue-100/30'
    "
  >
    {{ status }}
  </div>
</template>

<script>
export default {
  name: 'badge',

  props: {
    status: {
      type: String,
      required: false,
      default: 'kasutaja',
    },
  },
};
</script>
