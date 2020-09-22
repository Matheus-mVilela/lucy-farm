import React from 'react';
import { Text, View, StyleSheet, FlatList } from 'react-native';
import { Button } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';

import ItemCard from './ItemCard';


export default class ItemList extends React.Component {
  state = {
    items: []
  }

  componentDidMount() {
    const items = require('../../db.json').items.map(e => ({
      ...e
    }));
    this.setState({ items });
  }

  render() {
    return [
      <View style={styles.titleView}>
        <View style={styles.textView}>
          <Text style={styles.titleText}>Menu</Text>
        </View>
        <View>
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
      </View>,

      <FlatList
        key='flatlist'
        style={styles.list}
        data={this.state.items}
        renderItem={({ item }) => <ItemCard event={item} />}
        keyExtractor={item => item.id}
      />,
    ];
  }
}



const styles = StyleSheet.create({
  list: {
    flex: 1,
    backgroundColor: '#F3F3F3',
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
});
