<template>
    <Teleport to="body">
        <Transition name="modal-outer">
            <div class="fixed w-full bg-black bg-opacity-30 h-screen
            top-0 left-0 flex justify-center px-8"
            v-show="modalActive"
            @click.self="$emit('close-modal')">
                <Transition name="modal-inner">
                    <div class="p-4 bg-white self-start mt-32 h-3/4 w-[400px] rounded-xl"
                    v-if="modalActive">
                      <div class="flex flex-col text-2xl h-full justify-between items-center pl-2">
                        <div>
                        <div class="flex flex-row justify-between px-4 py-2 text-3xl">
                          <div>
                            Info ostja kohta
                          </div>
                          <img src="@/assets/alert-circle.svg" alt="XD" class="mb-2 cursor-pointer" @click="$emit('close-modal')">
                        </div>
                        <div class="mt-10 mb-10 flex flex-row">
                          <div class="mx-4">
                            Nimi:
                            <p class="text-xl mt-3">Placeholder</p>
                          </div>
                          <div class="mx-4">
                            Perekonnanimi:
                            <p class="text-xl mt-3">Placeholder</p>
                          </div>
                        </div>
                        <div class="flex flex-row">
                          <div class="flex flex-col mx-4">
                            Aadress:
                            <p class="text-xl mt-3">Placeholder</p>
                          </div>
                          <div class="flex flex-col mx-4">
                            Linn:
                            <p class="text-xl mt-3">Placeholder</p>
                          </div>
                        </div>
                        <div class="flex flex-row mt-10">
                          <div class="flex flex-col mx-4">
                            Postiindeks:
                            <p class="text-xl mt-3">Placeholder</p>
                          </div>
                        </div>
                        </div>
                        <div class="flex flex-row">
                          <button class="py-2 px-6 rounded-2xl bg-gray-200 mr-4"
                            @click="$emit('close-modal')"
                          >Katkesta</button>
                          <button @click="approve()" class="py-2 px-6 ml-4 bg-gray-600 border-black border-2 rounded-2xl text-white"
                          >Tehtud
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
import { usePostsStore } from '../store/modules/posts';

export default {
  data() {
    return {
      modalActive: false,
    }
  },
  props: {
    modalActive: Boolean,
  },
  methods: {
    approve() {
      // Add more!!!
      this.$emit('close-modal');
    }
  }
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