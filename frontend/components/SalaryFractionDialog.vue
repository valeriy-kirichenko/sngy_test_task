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
                  label="Ставка, руб"
                  variant="underlined"
                  v-model="salary"
                ></v-text-field> 
              </v-col>
              <v-col>
                <v-text-field
                  label="Ставка, %"
                  variant="underlined"
                  v-model="fraction"
                ></v-text-field> 
              </v-col>
            </v-row> 
            <v-row justify="space-around">
              <v-col>
                <v-btn
                  color="green"
                  variant="text"
                  @click="dialog = false">
                    Отменить
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  color="green"
                  :disabled="isValues(salary, fraction)"
                  type="submit"
                  variant="text"
                  @click="setSalaryFraction(
                    {
                      id: itemId,
                      salary: parseInt(salary),
                      fraction: parseInt(fraction)
                    }
                  ),
                  dialog = false">
                    Сохранить
                </v-btn>
              </v-col>
            </v-row>   
          </v-container>
        </v-form>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { ref } from 'vue'
import { SET_SALARY_FRACTION_MUTATION } from '~/queries/queries.js'

  export default {
    props: ['itemId', 'fireDate'],

    setup() {
        const { mutate: setSalaryFraction } = useMutation(
          SET_SALARY_FRACTION_MUTATION
        )

        const dialog = ref(Boolean)
        dialog.value = false

        const salary = ref('')
        const fraction = ref('')

        const isValues = function(salary, fraction) {
          return !(salary & fraction)
        }

        return {
            salary,
            fraction,
            dialog,
            setSalaryFraction,
            isValues
        }
    }
}
</script>
