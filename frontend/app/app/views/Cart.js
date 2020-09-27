import React from 'react';
import { Text, View, StyleSheet, FlatList, TouchableHighlight } from 'react-native';

import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';

import services from '../services';

export class Cart extends React.Component {
  state = {
    loading: false,
    items: [],
    total: undefined,
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
              icon={
                <Icon
                  onPress={() => this.props.navigation.goBack()}
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
          renderItem={({ item }) => <CartItem event={item} />}
          keyExtractor={item => item.id}
        />

        <View style={styles.footer}>
          {this.state.total !== undefined && (
            <Text>Total: {this.state.total}</Text>
          )}
          {this.state.total !== undefined && (
            <TouchableHighlight onPress={() => this.props.navigation.navigate('FinishOrder')}>
              <Text>FINALIZAR PEDIDO</Text>
            </TouchableHighlight>
          )}
        </View>
      </View >
    );
  }
}

function CartItem({ event }) {
  return (
    <View style={styles.cartList}>
      <View style={styles.cartItem}>
        <Text>{event.name}({event.measure})</Text>
      </View>
      <View>
        <Text>R${event.price}</Text>
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
  cartItem: {
    paddingRight: 100,
  },
  footer: {
    flex: 1
  },
});
