<template>
  <v-card class="px-10" >
    <v-data-table
      v-model="selected"
      :items="data.getOccupations"
      :headers="headers"
      :search="search"
      items-per-page-text="Строк на странице"
      show-select
      @item-selected="changedSelect(selected)"
    >
      <template v-slot:item.hireDate="{ item }">
        {{ setDate(item.raw.hireDate) }}
      </template>

      <template v-slot:item.fireDate="{ item }">
        {{ setDate(item.raw.fireDate) }}
      </template>

      <template v-slot:item.salary="{ item }">
        <SalaryFractionDialog :itemId="item.raw.id" :fireDate="item.raw.fireDate">
          {{ item.raw.salary.toLocaleString('ru') }} ₽
          ({{ item.raw.fraction }}%)
        </SalaryFractionDialog>
        <span v-if="item.raw.fireDate">
          {{ item.raw.salary.toLocaleString('ru') }} ₽
          ({{ item.raw.fraction }}%)
        </span>
      </template>

      <template v-slot:item.base="{ item }">
        <BaseDialog :itemId="item.raw.id" :fireDate="item.raw.fireDate">
          {{ item.raw.base.toLocaleString('ru') }} ₽
        </BaseDialog>
        <span v-if="item.raw.fireDate">
          {{ item.raw.base.toLocaleString('ru') }} ₽
        </span>
      </template>

      <template v-slot:item.advance="{ item }">
        <AdvanceDialog :itemId="item.raw.id" :fireDate="item.raw.fireDate">
          {{ item.raw.advance.toLocaleString('ru') }} ₽
        </AdvanceDialog>
        <span v-if="item.raw.fireDate">
          {{ item.raw.advance.toLocaleString('ru') }} ₽
        </span>
      </template>

      <template v-slot:item.byHours="{ item }">
        <v-checkbox-btn
          v-model="item.raw.byHours"
          @click="setByHours({id: item.raw.id, byHours: !item.raw.byHours})"
        ></v-checkbox-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
  import {
    GET_ALL_OCCUPATIONS_QUERY,
    SET_BY_HOURS_MUTATION
  } from '~/queries/queries.js'
  import AdvanceDialog from './AdvanceDialog'
  import BaseDialog from './BaseDialog'
  import SalaryFractionDialog from './SalaryFractionDialog'
  import { ref } from 'vue'

  export default {
    components: {AdvanceDialog, BaseDialog, SalaryFractionDialog},
    props: ["search"],

    setup(_, { emit }) {
      const { mutate: setByHours } = useMutation(SET_BY_HOURS_MUTATION)
      const { data } = useAsyncQuery(GET_ALL_OCCUPATIONS_QUERY)
      const selected = ref([])
      const headers = [
        {
          title: 'Сотрудники',
          key: 'name',
          align: 'start',
        },
        {title: 'Компания', key: 'companyName'},
        {title: 'Должность', key: 'positionName'},
        {title: 'Дата приёма', key: 'hireDate'},
        {title: 'Дата увольнения', key: 'fireDate'},
        {title: 'Ставка', key: 'salary'},
        {title: 'База', key: 'base'},
        {title: 'Аванс', key: 'advance'},
        {title: 'Почасовая', key: 'byHours'},
      ]

      const setDate = function(date) {
          if (date) {
              return date.split("-").reverse().join(".")
          }
      }

      const changedSelect = function(value) {
                emit('selected', value)
            }

      return {
        data,
        selected,
        headers,
        setDate,
        setByHours,
        changedSelect
      }
    }
  }
</script>
