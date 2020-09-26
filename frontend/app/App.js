import React from 'react';
import Login from './app/views/Login'
import Register from './app/views/Register'
import ItemList from './app/views/ItemList'
import CartView from './app/views/CartView'
import ConfirmView from './app/views/ConfirmView'


export default class App extends React.Component {
  render() {
    return (
      <CartView/>
    );
  }
}
