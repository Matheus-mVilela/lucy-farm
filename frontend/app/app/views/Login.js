import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import Header from "../sections/Header";
import Footer from "../sections/Footer";

export class Login extends React.Component {
  goToItemList = () => {
    this.props.navigation.navigate('Produtos')
  }

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

          <TouchableOpacity
            style={styles.btnLogin}
            onPress={this.goToItemList}
          >
            <Text style={styles.loginText}>LOGIN</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.btnRegister}
            onPress={() => this.props.navigation.navigate('Cadastro')}
          >
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
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  componentLogin: {
    flex: 1.5,
    alignItems: 'center'
  },
  input: {
    backgroundColor: '#dcdcdc',
    width: 300,
    fontSize: 18,
    marginBottom: 15,
    borderRadius: 10,
    padding: 12,
  },
  btnLogin: {
    backgroundColor: '#3e620a',
    width: 200,
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
    backgroundColor: '#ff0',
    width: 200,
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
