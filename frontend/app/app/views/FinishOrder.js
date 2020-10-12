import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';

import service from '../services.js';

export class FinishOrder extends React.Component {
  goToItemList = () => {
    service.cleanCart();
    this.props.navigation.navigate('Produtos');
  }

  render() {
    return (
      <View style={styles.container}>
        <Text>Pedido Finalizado Com Sucesso !!!</Text>
        <TouchableOpacity style={styles.buttonFinish} onPress={this.goToItemList}>
          <Text style={styles.txtBtnFinish}>Voltar para o menu</Text>
        </TouchableOpacity>
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonFinish: {
    marginTop: 15,
    backgroundColor:'#ff0',
    width: 200,
    fontSize: 18,
    borderRadius: 10,
    padding: 9,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
