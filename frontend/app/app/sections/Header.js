import React from 'react';
import { StyleSheet, Text, View, Image} from 'react-native';


export default class Header extends React.Component {
  render() {
    return (
      <View style={styles.headStyles}>
        <Image style={styles.headLogo} source={require('../../assets/trator.png')} />
      </View>
    );
  }
}


const styles = StyleSheet.create({
  headStyles:{
    flex:1,
    marginBottom:20,
  },

  headLogo:{
    justifyContent:'center',  
  },
  
})