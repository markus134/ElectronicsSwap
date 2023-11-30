<template>
    <Teleport to="body">
        <Transition name="modal-outer">
            <div class="fixed w-full bg-black bg-opacity-30 h-screen
            top-0 left-0 flex justify-center px-8"
            v-show="modalActive"
            @click.self="$emit('close-modal')">
                <Transition name="modal-inner">
                    <div class="p-4 bg-white self-start mt-32 h-3/4 w-5/6 rounded-xl"
                    v-if="modalActive">
                      <div class="flex flex-col text-2xl h-full justify-between pl-2">
                        <div>
                        <div class="flex flex-row justify-between px-8 py-2 text-3xl">
                          <div>
                            Kaebus
                          </div>
                          <img src="@/assets/alert-circle.svg" alt="XD" class="mb-2 cursor-pointer" @click="$emit('close-modal')">
                        </div>
                        <div class="mt-6 mb-1">
                          Pealkiri
                        </div>
                        <input placeholder="Pealkiri" class='pl-2 text-gray-400 border-gray-400 border-2 rounded-xl' style="width: 20%; min-width: 100px"/>
                        <div class="mt-6 mb-1">Kategooria</div>
                        <select class='pl-2 text-gray-400 border-gray-400 border-2 rounded-xl'>
                          <option>Ebasobiv sisu</option>
                          <option>Petukaubandus</option>
                          <option>Tehniline probleem</option>
                          <option>Probleem kvaliteediga</option>
                        </select>
                        <div class="mt-6 mb-1">Täpsustav info</div>
                        <textarea placeholder="Täpsustav info" class='pl-2 text-gray-400 border-gray-400 border-2 rounded-xl' style="resize: none; width: 100%; height: 40%"></textarea>
                        </div>
                        <div class="flex flex-row justify-between">
                          <button class="py-2 px-6 rounded-2xl bg-gray-200"
                            @click="$emit('close-modal')"
                          >Katkesta</button>
                          <button class="py-2 px-6 bg-gray-600 border-black border-2 rounded-2xl text-white"
                          >Esita Kaebus
                          </button>
                        </div>
                      </div>
                    </div>
                </Transition>
            </div>
        </Transition>
    </Teleport>
</template>

<script>
export default {
  data() {
    return {
      modalActive: false,
    }
  },
  props: {
    modalActive: Boolean,
  },
}
</script>

<style scoped>
.modal-outer-enter-active,
.modal-outer-leave-active,
.modal-inner-enter-active,
.modal-inner-leave-active {
    transition: opacity 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-outer-enter-from,
.modal-outer-leave-to,
.modal-inner-enter-from,
.modal-inner-leave-to {
    opacity: 0;
}
</style>