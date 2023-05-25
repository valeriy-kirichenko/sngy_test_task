<template>
  <v-row align="start" class="mb-5">
    <v-col cols="7">
      <v-card-title class="mt-5">
        Занимаемые должности
      </v-card-title>
    </v-col>
    <v-col>
      <v-card-text>
        <v-text-field
          v-model="search"
          @input="changed(search)"
          variant="underlined"
          label="Поиск по сотруднику"
          append-inner-icon="mdi-magnify"
          single-line
          hide-details
        ></v-text-field>
      </v-card-text>
      <v-row align="center" justify="space-around">
        <v-checkbox
          class="mr-2"
          hide-details label="Показывать уволенных">
        </v-checkbox> 
        <v-row >
          <v-col>
            <v-btn
              class="text-none text-black text-button pa-2"
              color="green-lighten-3"
            >
              Принять на должность
            </v-btn>
          </v-col>
          <v-col>
            <v-btn
              :disabled="!select"
              class="text-none text-black text-button pa-2"
              color="green-lighten-3"
            >
              Снять с должности {{ selected }}
            </v-btn>
          </v-col>
        </v-row>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
    import { ref } from 'vue'

    export default {
        props: ["selected"],
  
        setup(_, { emit }) {
            const search = ref('')
            const changed = (value) => {
                emit('search', value)
            }
            const isSelected = function() {
              if (!selected) {
                return true
              }
            }

            return {
              search,
              changed,
              isSelected
            }
        }
    }
</script>
