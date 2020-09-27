import React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';

import services from '../services';

export function ItemCard({ item }) {
  return (
    <View style={styles.card}>
      <View>
        <Text style={styles.name}>{item.name}</Text>
        <Text style={styles.measure}>{item.measure}</Text>
        <Text style={styles.price}>R${item.price}</Text>
      </View>
      <View style={styles.button}>
        <Button
          onPress={() => { services.addItemToCart(item) }}
          icon={
            <Icon
              name="plus"
              size={25}
              color="white"
            />
          }
        />
      </View>
    </View >
  );
}

const styles = StyleSheet.create({
  card: {
    borderBottomWidth: 2,
    borderBottomColor: 'black',
    padding: 15,
    paddingTop: 20,
    marginBottom: 5,
    flexDirection: 'row',
    justifyContent: "space-between"
  },
  button: {
    justifyContent: 'center',
  },
  name: {
    fontSize: 22,
    fontWeight: 'bold'
  },
  measure: {
    fontSize: 15,
    marginBottom: 10
  },
  price: {
    fontSize: 20,
  },
});
