import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import { Login } from './app/views/Login.js';
import { Register } from './app/views/Register.js';
import { ItemList } from './app/views/ItemList.js';
import { Cart } from './app/views/Cart.js';
import { FinishOrder } from './app/views/FinishOrder.js';


const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen
          name="Login"
          component={Login}
        />
        <Stack.Screen
          name="Cadastro"
          component={Register}
        />
        <Stack.Screen
          name="Produtos"
          component={ItemList}
        />
        <Stack.Screen
          name="Carrinho"
          component={Cart}
        />
        <Stack.Screen
          name="FinishOrder"
          component={FinishOrder}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
