import 'package:flutter/material.dart';


class AnnouncePage extends StatefulWidget {
  const AnnouncePage({Key? key}) : super(key: key);

  @override
  _AnnouncePage createState() => _AnnouncePage();
}

class _AnnouncePage extends State<AnnouncePage> {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
        child: Container(
          child: const Text(
            'Index 4: Объявления',
          ),
        )
    );
  }
}

