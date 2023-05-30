<template>
  <v-card class="px-10" >
    <v-data-table
      v-model="selected"
      @:change="changedSelect(selected)"
      :items="correctData(data.getOccupations)"
      :headers="headers"
      :search="search"
      :custom-filter="filterByName"
      item-key="id"
      items-per-page-text="Строк на странице"
      show-select
    >
      <template v-slot:item="{ item }">
        <tr v-if="showFired(fired, item.raw.fireDate)" :class="trClass(item.raw.fireDate)">
          <td>
            <v-checkbox
              v-model="selected"
              v-if="!item.raw.fireDate"
              
              :value="item.raw.id"
            />
          </td>
          <td>{{ item.raw.name }}</td>
          <td>{{ item.raw.companyName }}</td>
          <td>{{ item.raw.positionName }}</td>
          <td>{{ setDate(item.raw.hireDate) }}</td>
          <td>{{ setDate(item.raw.fireDate) }}</td>
          <td>
            <SalaryFractionDialog
              :itemId="item.raw.id"
              :fireDate="item.raw.fireDate"
            >
              {{ item.raw.salary.toLocaleString('ru') }} ₽
              ({{ item.raw.fraction.toLocaleString('ru') }}%)
            </SalaryFractionDialog>
            <span v-if="item.raw.fireDate">
              {{ item.raw.salary.toLocaleString('ru') }} ₽
              ({{ item.raw.fraction }}%)
            </span>
          </td>
          <td>
            <BaseDialog :itemId="item.raw.id" :fireDate="item.raw.fireDate">
              {{ item.raw.base.toLocaleString('ru') }} ₽
            </BaseDialog>
            <span v-if="item.raw.fireDate">
              {{ item.raw.base.toLocaleString('ru') }} ₽
            </span>
          </td>
          <td>
            <AdvanceDialog :itemId="item.raw.id" :fireDate="item.raw.fireDate">
              {{ item.raw.advance.toLocaleString('ru') }} ₽
            </AdvanceDialog>
            <span v-if="item.raw.fireDate">
              {{ item.raw.advance.toLocaleString('ru') }} ₽
            </span>
          </td>
          <td>
            <v-checkbox-btn
              :disabled="isFired(item.raw.fireDate)"
              v-model="item.raw.byHours"
              color="success"
              @click="setByHours(
                {id: item.raw.id, byHours: !item.raw.byHours}
              )"
            ></v-checkbox-btn>
          </td>
        </tr>
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
    props: ["search", "item", "fired"],

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
          {title: 'Дата приёма', key: 'sortableHireDate'},
          {title: 'Дата увольнения', key: 'sortableFireDate'},
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

      const trClass = function(fire) {
          if (fire) {
              return "red"
          }
      }

      const showFired = function(fired, data) {
          if (fired) {
              return true
          }
          if (!fired && data) {
              return false
          }
          else {
              return true
          }
      }

      const isFired = function(fired) {
          if (fired) {
              return true
          }
      }

      const filterByName = function(_, query, { raw }) {
          return raw.name.toLowerCase().includes(query.toLowerCase())
      }

      const correctData = function(data) {
          console.log(data)
          return data.map((d) => {
            return {
              ...d,
              sortableFireDate: sortableDate(d.fireDate),
              sortableHireDate: sortableDate(d.hireDate),
            }
          })
      }

      const sortableDate = function(date) {
          if (!date) {
              return "0"
          }
          else {
              return date
          }
      }


      return {
        data,
        selected,
        headers,
        setDate,
        setByHours,
        changedSelect,
        trClass,
        showFired,
        isFired,
        filterByName,
        correctData
      }
    }
  }
</script>

<style scoped>
  .red td {background-color:rgb(254, 124, 124) !important;}
</style>
