import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, FlatList } from 'react-native';
import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome'

export default class Login extends React.Component {
  render() {
    const dados = [
      { key: 'Linha 0',valor:'R$10'},
      { key: 'Linha 1',valor:'R$10'}, 
      { key: 'Linha 2',valor:'R$10'}, 
      { key: 'Linha 3',valor:'R$10'}, 
      { key: 'Linha 4',valor:'R$10'}, 
      { key: 'Linha 5',valor:'R$10'}, 
      { key: 'Linha 6',valor:'R$10'}, 
      { key: 'Linha 7',valor:'R$10'}, 
      { key: 'Linha 8',valor:'R$10'}, 
      { key: 'Linha 9',valor:'R$10'}, 
    ]

    return (
      <View style={styles.container}>
        <View style={styles.grupCart} >
          <View style={styles.cartView}>
            <Text style={styles.txtView}>Carrinho</Text>
          </View>
          <View style={styles.btnView}>
            <Button
              icon={
                <Icon
                  name="shopping-cart"
                  size={25}
                  color="white"
                />
              }
            />
          </View>

        </View>

        <View style={styles.viewList}>
          <FlatList
            data={dados}
            renderItem={({ item }) => <Text style={styles.textList}>{item.key}{item.valor}</Text>}
          />
        </View>

        <View style={styles.valorTotalView}>
          <Text style={styles.textTotal}>R$100,00</Text>
          <Text style={styles.textTotal}>Total</Text>

        </View>

        <View style={styles.btnFinishView}>
          <TouchableOpacity style={styles.btnfinish}>
            <Text style={styles.finishText}>Finalizar Pedido!</Text>
          </TouchableOpacity>
        </View>

      </View>

    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex:1,
  },
  grupCart: {
    paddingTop: 45,
    paddingBottom: 20,
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    paddingLeft: 25,
    paddingRight: 25,
  },
  cartView: {
    flex: 1,
    alignItems: "center",
  },

  txtView: {
    flex: 1,
    fontSize: 35,
    fontWeight: '800',
  },
  btnFinishView: {
    flex:0.5,
    alignItems: 'center',
    justifyContent: 'flex-end'
  },
  btnfinish: {
    width: '80%',
    padding: 12,
    borderRadius: 20,
    marginBottom: 55,
    alignItems: 'center',
    backgroundColor: '#228B22',
  },
  finishText: {
    fontSize: 25,
    color: '#fff',

  },
  viewList:{
    flex:1,
    
  },
  textList:{
    fontSize:23,
    padding:7,
    borderWidth:0.5,
  },

  valorTotalView:{
    flex:0.2,
    alignItems:'center',
    justifyContent:"center",
  },

  textTotal:{
    fontSize:30,
  }
});