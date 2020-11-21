import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import React from 'react';

import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

// Screens
import SigninScreen from './src/screens/Signin';
import SignupScreen from './src/screens/Signup';

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Signin"
          component={SigninScreen}
        />
        <Stack.Screen
          name="Signup"
          component={SignupScreen}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
