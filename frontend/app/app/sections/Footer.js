import React from 'react';
import { StyleSheet, Image, View,} from 'react-native';


export default class Header extends React.Component {
  render() {
    return (
      <View style={styles.footertyles}>
        <Image style={styles.headLogo} source={require('../../assets/gramad.png')} />
      </View>
    );
  }
}


const styles = StyleSheet.create({
  footertyles:{
    flex:0.5,
    width:'100%',
    borderTopLeftRadius:400,
    borderTopRightRadius:400,
  },

  headLogo:{
    justifyContent:'center',  
  },
  
})