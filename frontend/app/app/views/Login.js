import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import Header from "../sections/Header";
import Footer from "../sections/Footer";

export default class Login extends React.Component {
  render() {
    return (
      <View style={styles.container}>

        <Header />

        <View style={styles.componentLogin}>
          <TextInput
            style={styles.input}
            placeholder="username ou email"
            autoCorrect={false}
            onChangeText={() => { }}
          />

          <TextInput
            style={styles.input}
            placeholder="password"
            autoCorrect={false}
            onChangeText={() => { }}
          />

          <TouchableOpacity style={styles.btnLogin}>
            <Text style={styles.loginText}>LOGIN</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.btnRegister}>
            <Text style={styles.registerText}>FAZER CADASTRO</Text>
          </TouchableOpacity>
        </View>

        <Footer />
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex:1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  componentLogin:{
    flex:1.5,
    alignItems:'center'
  },
  input: {
    backgroundColor: '#dcdcdc',
    width:300,
    fontSize: 18,
    marginBottom: 15,
    borderRadius: 10,
    padding: 12,
  },
  btnLogin: {
    backgroundColor: '#228B22',
    width:200,
    fontSize: 18,
    marginTop: 22,
    borderRadius: 10,
    padding: 9,
    alignItems: 'center',
    justifyContent: 'center',
  },
  loginText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold'
  },
  btnRegister: {
    marginTop: 15,
    backgroundColor: '#1E90FF',
    width:200,
    fontSize: 18,
    borderRadius: 10,
    padding: 9,
    alignItems: 'center',
    justifyContent: 'center',
  },
  registerText: {
    color: '#080101',
  }


});