export const GET_ALL_OCCUPATIONS_QUERY = gql`
    query getOccupations {
        getOccupations {
            id
            name
            companyName
            positionName
            salary
            fraction
            base
            advance
            byHours
            hireDate
            fireDate
        }
    }
`

export const SET_BY_HOURS_MUTATION = gql`
    mutation UpdateOccupationMutation ($id: ID! $byHours: Boolean!) {
        updateOccupation (id: $id byHours: $byHours) {
                occupation {
                    name
                    companyName
                    positionName
                    salary
                    fraction
                    base
                    advance
                    byHours
                    hireDate
                    fireDate
                }
            }
    }
`

export const SET_ADVANCE_MUTATION = gql`
    mutation UpdateOccupationMutation ($id: ID! $advance: Int!) {
        updateOccupation (id: $id advance: $advance) {
                occupation {
                    name
                    companyName
                    positionName
                    salary
                    fraction
                    base
                    advance
                    byHours
                    hireDate
                    fireDate
                }
            }
    }
`

export const SET_BASE_MUTATION = gql`
    mutation UpdateOccupationMutation ($id: ID! $base: Int!) {
        updateOccupation (id: $id base: $base) {
                occupation {
                    name
                    companyName
                    positionName
                    salary
                    fraction
                    base
                    advance
                    byHours
                    hireDate
                    fireDate
                }
            }
    }
`

export const SET_SALARY_FRACTION_MUTATION = gql`
    mutation UpdateOccupationMutation ($id: ID! $salary: Int! $fraction: Int!) {
        updateOccupation (id: $id salary: $salary fraction: $fraction) {
                occupation {
                    name
                    companyName
                    positionName
                    salary
                    fraction
                    base
                    advance
                    byHours
                    hireDate
                    fireDate
                }
            }
    }
`

export const SET_FIRE_DATE_MUTATION = gql`
mutation FireOccupationMutation ($id: Int!) {
    fireOccupation (id: $id) {
            occupation {
                name
                companyName
                positionName
                salary
                fraction
                base
                advance
                byHours
                hireDate
                fireDate
            }
    }
}
`
