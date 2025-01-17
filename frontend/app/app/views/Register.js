import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import Header from "../sections/Header";
import Footer from "../sections/Footer";

export class Register extends React.Component {
  goBack = () => {
    this.props.navigation.goBack()
  }

  render() {
    return (
      <View style={styles.container}>

        <Header />

        <View style={styles.componentLogin}>
          <TextInput
            style={styles.input}
            placeholder="username"
            autoCorrect={false}
            onChangeText={() => { }}
          />

          <TextInput
            style={styles.input}
            placeholder="email"
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
            style={styles.btnRegister}
            onPress={this.goBack}
          >
            <Text style={styles.registerText}>FAZER CADASTRO</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.btnRegister}
            onPress={this.goBack}
          >
            <Text style={styles.registerText}>Voltar</Text>
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
