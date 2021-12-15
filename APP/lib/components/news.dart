import 'package:flutter/material.dart';


class NewsPage extends StatefulWidget {
  const NewsPage({Key? key}) : super(key: key);

  @override
  _NewsPage createState() => _NewsPage();
}

class _NewsPage extends State<NewsPage> {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
        child: Container(
          child: const Text(
            'Index 3: Лента',
          ),
        )
    );
  }
}

