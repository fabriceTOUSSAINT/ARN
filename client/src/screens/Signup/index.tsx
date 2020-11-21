import React from 'react';
import { Text, View, StyleSheet, TouchableOpacity } from 'react-native';

// interface SignupProps {
//     navigation: any
// }

const Signup = ({ navigation, ...props }: any) => {
    return (
        <View style={styles.container}>
            <Text style={styles.boldText}>Signup</Text>
            <TouchableOpacity onPress={() => navigation?.navigate('Signin')}>
                <Text style={styles.boldText}>Sign in instead</Text>
            </TouchableOpacity>
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

export default Signup;