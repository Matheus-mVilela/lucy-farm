import React from 'react';
import { Text, View, StyleSheet, FlatList, TouchableOpacity } from 'react-native';

import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';

import services from '../services';

export class Cart extends React.Component {
  state = {
    loading: false,
    items: [],
    total: 0,
  }

  componentDidMount() {
    this.setState({ loading: true });
    services.loadCart().then(card => {
      this.setState({ items: card.items, total: card.total });
      this.setState({ loading: false });
    })
  }

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.titleView}>
          <View style={styles.textView}>
            <Text style={styles.titleText}>CARRINHO</Text>
          </View>
          <View>
            <Button
              onPress={() => this.props.navigation.goBack()}
              icon={
                <Icon
                  name="plus"
                  size={25}
                  color="white"
                />
              }
            />
          </View>
        </View>

        {this.state.loading && (
          <Text>Loading data from server...</Text>
        )}

        <FlatList
          key='flatlist'
          style={styles.list}
          data={this.state.items}
          renderItem={({ item }) => <CartItem item={item} />}
          keyExtractor={item => item.id}
        />

        <View style={styles.footer}>
          {this.state.total !== 0 && (
            <Text>Total: {this.state.total}</Text>
          )}
          {this.state.total !== 0 && (
            <TouchableOpacity style={styles.buttonFinish} onPress={() => this.props.navigation.navigate('FinishOrder')}>
              <Text style={styles.txtBtnFinish}>FINALIZAR PEDIDO</Text>
            </TouchableOpacity>
          )}
        </View>
      </View >
    );
  }
}

function CartItem({ item }) {
  return (
    <View style={styles.cartList}>
      <View style={styles.removeItem}>
        <Button
          onPress={() => services.removeItemToCart(item.id)}
          icon={
            <Icon
              name="close"
              size={20}
              color="white"
            />
          }
        />
      </View>
      <View style={styles.cartItem}>
        <Text>{item.name}({item.measure})</Text>
      </View>
      <View>
        <Text>R${item.price}</Text>
      </View>
    </View >
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  titleView: {
    paddingTop: 45,
    paddingBottom: 20,
    backgroundColor: '#778899',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    paddingLeft: 25,
    paddingRight: 25,
  },
  textView: {
    flex: 1,
  },
  titleText: {
    fontSize: 40,
    fontWeight: 'bold',
    color: 'white',
  },
  list: {
    marginTop: 200,
    flex: 1,
    backgroundColor: '#F3F3F3',
  },
  cartList: {
    alignItems: 'flex-end',
    borderBottomWidth: 1,
    borderBottomColor: 'black',
    flexDirection: 'row',
    justifyContent: 'flex-end',
  },
  removeItem: {
    paddingRight: 10,
  },
  cartItem: {
    paddingRight: 100,
  },
  buttonFinish: {
    marginTop: 15,
    backgroundColor: 'green',
    width: 200,
    fontSize: 18,
    borderRadius: 10,
    padding: 9,
    alignItems: 'center',
    justifyContent: 'center',
  },
  txtBtnFinish:{
    color:'#fff',
  },
  footer: {
    flex: 1,
    marginTop: 50
  },
});
