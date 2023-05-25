<template>
  <div>
    <v-dialog v-if="!fireDate" v-model="dialog" width="auto">
      <template v-slot:activator="{ props }">
        <span v-bind="props"><slot></slot></span>
      </template>
      <v-card>
        <v-form>
        <v-container>
          <v-row>
            <v-col>
              <v-text-field
                label="Аванс, руб"
                variant="underlined"
                v-model="advance"
              ></v-text-field> 
            </v-col>
          </v-row> 
          <v-row justify="space-around">
            <v-col>
              <v-btn color="green" variant="text" @click="dialog = false">
                Отменить
              </v-btn>
            </v-col>
            <v-col>
              <v-btn
                color="green"
                :disabled="!advance"
                type="submit"
                variant="text"
                @click="setAdvance({id: itemId, advance: parseInt(advance)}),
                dialog = false">
                Сохранить
              </v-btn>
            </v-col>
          </v-row>   
        </v-container></v-form>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { ref } from 'vue'
import { SET_ADVANCE_MUTATION } from '~/queries/queries.js'

  export default {
    props: ['itemId', 'fireDate'],

    setup() {
        const { mutate: setAdvance } = useMutation(SET_ADVANCE_MUTATION)

        const dialog = ref(Boolean)
        dialog.value = false

        const advance = ref('')

        return {
            advance,
            dialog,
            setAdvance
        }
    }
}
</script>