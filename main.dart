import 'package:flutter/material.dart';
void main() => runApp(sudoku());

class sudoku extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sudoku',
      debugShowCheckedModebanner: false,
      theme: Themedata(fontFamily: 'Roboto'),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(

    );
  }
}