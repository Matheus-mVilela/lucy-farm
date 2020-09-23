import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome'

export default class Login extends React.Component {
  render() {
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
        
        <View>

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
  container:{
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
    flex:1,
    alignItems:'center', 
    justifyContent:'flex-end' 
  },
  btnfinish:{
    width:'80%',
    padding:12,
    borderRadius:20,
    marginBottom:55,
    alignItems:'center',
    backgroundColor:'#228B22',
  },
  finishText:{
    fontSize:25,
    color:'#fff',
    
  },


});