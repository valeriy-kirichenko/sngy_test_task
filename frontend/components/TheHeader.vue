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
          color="success"
          v-model="show"
          class="mr-2"
          hide-details label="Показывать уволенных"
          @change="showFired(show)"
        >  
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
            <v-form>
              <v-btn
                :disabled="selected.length === 0"
                class="text-none text-black text-button pa-2"
                color="rgb(254, 124, 124)"
                type="submit"
                @click="fire(selected)"
              >
                <span v-if="selected.length <= 1">Снять с должности</span>
                <span v-else>Снять с должностей</span> 
              </v-btn>
            </v-form>
            
          </v-col>
        </v-row>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
    import { ref } from 'vue'
    import { SET_FIRE_DATE_MUTATION } from '~/queries/queries.js'

    export default {
        props: ["selected"],
  
        setup(_, { emit }) {
            const search = ref('')
            const show = ref()
            const changed = (value) => {
              emit('search', value)
            }
            const showFired = (value) => {
              emit('showFired', value)
            }

            const { mutate: setFireDate} = useMutation(SET_FIRE_DATE_MUTATION)

            const fire = function(selected) {
              for (let id in selected) {
                setFireDate({id: parseInt(selected[id])})
              }
            }

            return {
              search,
              changed,
              show,
              showFired,
              setFireDate,
              fire,
            }
        }
    }
</script>

<style scoped>
  .v-btn--disabled.v-btn--variant-elevated, .v-btn--disabled.v-btn--variant-flat {
    background-color: #DDE5ED !important;
    color: rgba(0, 0, 0, 0.437) !important;
  }
  .v-btn {
    font-weight: 600;
  }
</style>
