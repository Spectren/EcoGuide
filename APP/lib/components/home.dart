import 'package:flutter/material.dart';
import 'package:eco_guide/components/ecoguide.dart';


class Profile extends StatefulWidget {
  @override
  _Profile createState() => _Profile();
}

int _selectedIndex = 1;
List<Widget> _widgetList = <Widget>[
  EcoGuidePage(),
  //new HomePage(),
  //new NewsPage(),
  //new AnnouncePage(),
  //new MapPage()
];

class _Profile extends State<Profile> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _widgetList.elementAt(_selectedIndex),
      bottomNavigationBar: BottomNavigationBar(
          items: const <BottomNavigationBarItem>[
            BottomNavigationBarItem(
              icon: Icon(
                Icons.account_circle,
                color: Colors.white,
              ),
              label: "Главная",
              activeIcon: Icon(
                Icons.account_circle,
                color: Colors.yellow,
              ),
            ),
            BottomNavigationBarItem(
              icon: Icon(
                Icons.account_circle,
                color: Colors.white,
              ),
              label: "Экогид",
              activeIcon: Icon(
                Icons.account_circle,
                color: Colors.yellow,
              ),
            ),
            BottomNavigationBarItem(
              icon: Icon(
                Icons.account_circle,
                color: Colors.white,
              ),
              label: "Лента",
              activeIcon: Icon(
                Icons.account_circle,
                color: Colors.yellow,
              ),
            ),
            BottomNavigationBarItem(
              icon: Icon(
                Icons.account_circle,
                color: Colors.white,
              ),
              label: "Объявления",
              activeIcon: Icon(
                Icons.account_circle,
                color: Colors.yellow,
              ),
            ),
          ],
          backgroundColor: Colors.black,
          unselectedItemColor: Colors.white,
          selectedItemColor: Colors.yellow,
          currentIndex: _selectedIndex,
          onTap: (int index) {
            setState(() {
              _selectedIndex = index;
            });
          }),
    );
  }
}
