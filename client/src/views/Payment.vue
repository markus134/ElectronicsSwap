<template>
  <div class="relative h-screen w-full">
    <Navbar />
    <div class="w-full h-full flex items-center justify-center gap-x-6">
      <div class="flex flex-col gap-y-1.5 items-center">
        <button
          class="transition-all text-sm font-semibold"
          :class="step == 1 ? 'text-[#B4BEEF]' : 'text-gray-600/20'"
          @click="step = 1"
        >
          Arveldusteave
        </button>
        <div
          class="transition-all h-12 w-px border"
          :class="step == 1 ? 'border-[#B4BEEF]' : 'border-gray-600/10'"
        ></div>
        <button
          class="transition-all text-sm font-semibold"
          :class="
            step == 2
              ? 'text-[#B4BEEF]'
              : step > 2
              ? 'text-gray-600/20'
              : 'text-gray-600/70'
          "
          @click="!isErrorInFirstStep ? (step = 2) : null"
        >
          Kaarditeave
        </button>
        <div
          class="transition-all h-12 w-px border border-[#B4BEEF]"
          :class="
            step == 2
              ? 'border-[#B4BEEF]'
              : step > 2
              ? 'border-gray-600/20'
              : 'border-gray-600/50'
          "
        ></div>
        <button
          class="transition-all text-sm font-semibold"
          :class="step == 3 ? 'text-[#B4BEEF]' : 'text-gray-600/70'"
          @click="step = 3"
        >
          Kinnitamine
        </button>
      </div>
      <div class="flex flex-col gap-y-6">
        <div class="flex flex-col gap-y-6" v-if="step == 1">
          <h3 class="text-2xl text-black font-semibold">Arveldusteave</h3>
          <div class="flex flex-col gap-y-6">
            <div
              class="flex flex-col gap-y-3"
              :key="i"
              v-for="(input, i) in inputs"
            >
              <label
                :for="input.name"
                class="text-sm text-gray-300 capitalize"
                >{{ input.name }}</label
              >
              <input
                type="text"
                :id="input.name"
                class="transition-all pb-1.5 text-xl border-b border-gray-200 hover:border-gray-300 focus:border-gray-500 outline-none"
                :placeholder="`Sinu ${input.name}`"
                v-model="input.input"
              />
            </div>
          </div>
        </div>
        <div class="flex flex-col gap-y-6" v-if="step == 2">
          <div
            class="min-h-[320px] w-full max-w-[564px] p-6 flex justify-end gap-y-5 flex-col border rounded-3xl shadow-lg"
          >
            <div class="flex gap-x-6 items-center" v-if="paymentSystem">
              <img :src="paymentSystem.image" class="w-20 appear" alt="" />
              <p class="capitalize text-xl">{{ paymentSystem.name }}</p>
            </div>
            <div class="items-start flex flex-col gap-y-1.5">
              <label class="text-base" for="cardnumber">Card number</label>
              <input
                type="text"
                id="cardnumber"
                class="outline-none"
                :class="card.state == 'error' ? 'border-b border-red-600' : ''"
                placeholder="XXXX XXXX XXXX XXXX"
                v-model="card.number"
              />
              <!-- Delete this line code after -->
              <p class="text-sm text-gray-600/30">
                use <span class="font-bold">5247 0192 4931 3190</span> for dev
              </p>
            </div>
            <div class="items-start flex flex-col gap-y-1.5">
              <label class="text-base" for="cardholdername"
                >Cardholder name</label
              >
              <input
                type="text"
                id="cardholdername"
                class=""
                placeholder="Ina Hogan"
                v-model="card.holderName"
                ref="cardHolderInput"
              />
            </div>
            <div class="flex items-center justify-between gap-x-6">
              <div class="flex items-center gap-x-64">
                <div class="flex flex-col gap-y-1.5">
                  <label for="valid">Valid</label>
                  <div class="flex">
                    <input
                      type="text"
                      id="valid"
                      class="w-10 text-center placeholder:text-center"
                      placeholder="DD"
                      v-model="card.validDay"
                      ref="validDay"
                    />
                    <p>:</p>
                    <input
                      type="text"
                      id="valid"
                      class="w-10 text-center placeholder:text-center"
                      placeholder="MM"
                      v-model="card.validMonth"
                      ref="validMonth"
                    />
                  </div>
                </div>
                <div class="flex flex-col gap-y-1.5">
                  <label for="cvv">CVV</label>
                  <input
                    type="text"
                    id="cvv"
                    class="w-10 placeholder:text-center"
                    placeholder="XXX"
                    v-model="card.cvv"
                    ref="cvv"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-col gap-y-6" v-if="step == 3">
          <ul class="p-3 border rounded-lg">
            List of items
          </ul>
          <p>Total price:</p>
        </div>
        <div class="w-full flex gap-x-3">
          <button
            class="w-full px-9 py-3 border text-black disabled:opacity-50 disabled:cursor-not-allowed rounded-lg"
            :disabled="step == 1"
            @click="step -= 1"
          >
            Tagasi
          </button>
          <button
            class="w-full px-9 py-3 bg-[#B4BEEF] text-white disabled:opacity-50 disabled:cursor-not-allowed rounded-lg"
            :disabled="buttonNotAvailable"
            @click="step == 3 ? $router.push('/kinnitus') : (step += 1)"
            ref="continueButton"
          >
            {{ step == 3 ? "Kinnita" : "Edasi" }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import {
  Visa,
  Mastercard,
  Amex,
  Discover,
  DinersClub,
  JCB,
  UnionPay,
} from "@/assets";
export default {
  components: {
    Navbar,
  },

  data: () => ({
    step: 1,
    paymentSystems: {
      visa: {
        availableMII: [4],
        name: "visa",
        image: Visa,
      },
      mastercard: {
        availableMII: [5],
        name: "mastercard",
        image: Mastercard,
      },
      amex: {
        availableMII: [34, 37],
        name: "american express",
        image: Amex,
      },
      discover: {
        availableMII: [6],
        name: "discover",
        image: Discover,
      },
      dinersClub: {
        availableMII: [36, 55],
        name: "diners club",
        image: DinersClub,
      },
      jcb: {
        availableMII: [35],
        name: "jcb",
        image: JCB,
      },
      unionPay: {
        availableMII: [62],
        name: "union pay",
        image: UnionPay,
      },
    },
    card: {
      number: "",
      holderName: "",
      validMonth: "",
      validDay: "",
      cvv: "",
      state: "empty",
    },
    inputs: [
      { name: "eesnimi", input: "" },
      { name: "perekonnanimi", input: "" },
      { name: "address", input: "" },
      { name: "linn", input: "" },
      { name: "sihtnumber", input: "" },
    ],
    isInputChanged: false,
  }),

  watch: {
    "card.number"(value, old) {
      if (!value) {
        return;
      }
      if (value.length > 19) {
        this.card.number = old;
        this.$refs.cardHolderInput.focus();
        return;
      }
      value = value.replace(/[^0-9]/gi, "");
      this.card.number = value
        .match(/(\d{1,4})/g)
        .join(" ")
        .trim();
      this.card.state = this.isCardNumberValid(value);
    },

    "card.validDay"(value, old) {
      if (value.length > 2) {
        this.card.validDay = old;
      }
      if (value.length == 2) {
        this.$refs.validMonth.focus();
      }
    },

    "card.validMonth"(value, old) {
      if (value.length > 2) {
        this.card.validMonth = old;
      }
      if (value.length == 2) {
        this.$refs.cvv.focus();
      }
    },

    "card.cvv"(value, old) {
      if (value.length > 3) {
        this.card.cvv = old;
      }
      if (value.length == 3) {
        this.$refs.continueButton.focus();
      }
    },
  },

  computed: {
    buttonNotAvailable() {
      if (this.isErrorInFirstStep && this.step == 1) {
        return true;
      }

      if (this.isErrorInSecondStep && this.step == 2) {
        return true;
      }

      return false;
    },

    isErrorInFirstStep() {
      return this.inputs.map((elem) => !!elem.input).includes(false);
    },

    isErrorInSecondStep() {
      const isNotCompleted = Object.values(this.card)
        .map((elem) => !!elem)
        .includes(false);
      const { validDay, validMonth, cvv, state } = this.card;
      return !(
        !isNotCompleted &&
        state == "correct" &&
        validDay.length == 2 &&
        validMonth.length == 2 &&
        cvv.length == 3
      );
    },

    paymentSystem() {
      let availablePaymentSystems = [];
      for (let value of Object.values(this.paymentSystems)) {
        availablePaymentSystems = availablePaymentSystems.concat(
          value.availableMII
        );
      }
      availablePaymentSystems = availablePaymentSystems.sort((a, b) => b - a);
      const availablePaymentSystemsString = availablePaymentSystems.join("|");
      const regexValue = new RegExp(`^(?:${availablePaymentSystemsString})`);
      const paymentSystemBIN = this.card.number.match(regexValue);
      if (!paymentSystemBIN) {
        return null;
      }
      for (let [name, value] of Object.entries(this.paymentSystems)) {
        if (value.availableMII.includes(+paymentSystemBIN)) {
          return this.paymentSystems[name];
        }
      }
      return null;
    },
  },

  methods: {
    isCardNumberValid(cardNumber) {
      if (cardNumber.length == 0) {
        return "empty";
      }
      if (cardNumber.length < 12) {
        return "error";
      }
      const cardNumberArray = cardNumber.split("");
      let sum = 0;
      for (let i = 0; i < cardNumberArray.length; i++) {
        if (i % 2 != 0) {
          sum += +cardNumber[i];
          continue;
        }
        let doubleNum = +cardNumber[i] * 2;
        sum +=
          doubleNum >= 10
            ? +String(doubleNum)[0] + +String(doubleNum)[1]
            : doubleNum;
      }
      return sum % 10 == 0 ? "correct" : "error";
    },
  },
};
</script>

<style lang="scss" scoped>
.appear {
  animation: appear 0.2s ease-in-out forwards;
}

@keyframes appear {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>
