import 'package:flutter/material.dart';
import 'package:eco_guide/components/ecoguide.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "EcoGuide",
        theme: ThemeData(
          primarySwatch: Colors.green,
        ),
        home: EcoGuidePage());
  }
}
