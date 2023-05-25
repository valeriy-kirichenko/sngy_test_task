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
                label="База, руб"
                variant="underlined"
                v-model="base"
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
                :disabled="!base"
                type="submit"
                variant="text"
                @click="setBase({id: itemId, base: parseInt(base)}),
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
import { SET_BASE_MUTATION } from '~/queries/queries.js'

  export default {
    props: ['itemId', 'fireDate'],
    setup() {
        const { mutate: setBase } = useMutation(SET_BASE_MUTATION)

        const dialog = ref(Boolean)
        dialog.value = false

        const base = ref('')

        return {
            base,
            dialog,
            setBase
        }
    }
}
</script>