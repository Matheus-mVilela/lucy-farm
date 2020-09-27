import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';


export class FinishOrder extends React.Component {
  goToItemList = () => {
    this.props.navigation.navigate('Produtos')
  }

  render() {
    return (
      <View style={styles.container}>
        <Text>Pedido Finalizado Com Sucesso !!!</Text>
        <TouchableOpacity onPress={this.goToItemList}>
          <Text>Voltar para o menu</Text>
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
});
