import React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';
import Cart from '../views/Cart'


function addItmCart(){
      
}

export default function ItemCard({ event }) {
  return (
    <View style={styles.card}>
      <View>
        <Text style={styles.name}>{event.name}</Text>
        <Text style={styles.measure}>{event.measure}</Text>
        <Text style={styles.price}>R${event.price}</Text>
      </View>
      <View style={styles.button}>
        <Button onPress={(addItmCart(ItemCard))}
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
