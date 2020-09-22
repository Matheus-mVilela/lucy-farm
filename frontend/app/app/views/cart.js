import { createAction, createReduce } from '@reduxjs/toolkit'

const INICIAL_STATE = []

export const addItem = createAction('ADD_ITEMS')
export const removeItem = createAction('REMOVE_ITEMS')


export default createReduce(INICIAL_STATE, {
    [addItem.type]:(state, action) => [... state, action, payload],
    [removeItem.type]:(state, action) => state.filter(item => item.id !== action.payload)
});