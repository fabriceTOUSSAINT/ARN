import React from 'react';
import { Text, View, StyleSheet, TouchableOpacity, Button } from 'react-native';

// interface SigninProps {
//     navigation: any
// }

const Signin = ({ navigation, ...props }: any) => {

    const handleSignin = () => {
        console.log('here')
        navigation.navigate('Signup')
    }

    return (
        <View style={styles.container}>
            <Text style={styles.boldText}>Signin</Text>
            <Button onPress={handleSignin} title="sign_in_here">Sign in here</Button>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1, 
        backgroundColor: '#333',
        justifyContent: 'center',
        alignItems: 'center'
    },
    boldText: {
        color: '#fff',
        fontSize: 24,
        fontWeight :'bold'
    }
});

export default Signin;