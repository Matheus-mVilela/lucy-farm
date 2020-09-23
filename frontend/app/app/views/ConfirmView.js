import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome'

export default class Login extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.successtView}>
            <Text style={styles.txtSuccess}>Pedido Foi Enviado com Sucesso ! </Text>
        </View>

        <View style={styles.btnFinishView}>
          <TouchableOpacity style={styles.btnfinish}>
            <Text style={styles.finishText}>Voltar para Menu !</Text>
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
  successtView:{
      flex:1,
      alignItems:'center',
      justifyContent:'center',           
  },
  txtSuccess:{
      fontSize:40,
      fontWeight:'700',
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
    marginBottom:100,
    alignItems:'center',
    backgroundColor:'#1E90FF',
  },
  finishText:{
    fontSize:25,
    color:'#fff',
    
  },


});