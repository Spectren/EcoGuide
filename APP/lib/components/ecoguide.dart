import 'package:flutter/material.dart';


class EcoGuidePage extends StatefulWidget {
  const EcoGuidePage({Key? key}) : super(key: key);

  @override
  _EcoGuidePage createState() => _EcoGuidePage();
}

class _EcoGuidePage extends State<EcoGuidePage> {


  @override
  Widget build(BuildContext context) {
    return Container(
        margin: const EdgeInsets.all(15.0),
        child: ListView(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              // mainAxisSize: MainAxisSize.max,
              children: <Widget>[
                Column(
                  children: [
                    SizedBox(
                      width: MediaQuery.of(context).size.width * 0.2,
                      height: MediaQuery.of(context).size.height * 0.1,
                      child: IconButton(
                        onPressed: () {},
                        icon: Image.asset("assets/icons/food.png", fit:BoxFit.fill)
                      ),
                    ),
                    Text("Техника")
                  ],
                ),
                Column(
                  children: [
                    SizedBox(
                      width: MediaQuery.of(context).size.width * 0.2,
                      height: MediaQuery.of(context).size.height * 0.1,
                      child: IconButton(
                          onPressed: () {},
                          icon: Image.asset("assets/icons/hydro.png", fit:BoxFit.fill)
                      ),
                    ),
                    Text("Стелкло")
                  ],
                ),
                Column(
                  children: [
                    SizedBox(
                      width: MediaQuery.of(context).size.width * 0.2,
                      height: MediaQuery.of(context).size.height * 0.1,
                      child: IconButton(
                          onPressed: () {},
                          icon: Image.asset("assets/icons/reusable.png", fit:BoxFit.fill)
                      ),
                    ),
                    Text("Пластик")
                  ],
                ),
                Column(
                  children: [
                    SizedBox(
                      width: MediaQuery.of(context).size.width * 0.2,
                      height: MediaQuery.of(context).size.height * 0.1,
                      child: IconButton(
                          onPressed: () {},
                          icon: Image.asset("assets/icons/hydro.png", fit:BoxFit.fill)
                      ),
                    ),
                    Text("Батарейки")
                  ],
                ),
              ]
            ),
            const Padding(padding: EdgeInsets.only(bottom: 20)),
            Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  Column(
                    children: [
                      SizedBox(
                        width: MediaQuery.of(context).size.width * 0.2,
                        height: MediaQuery.of(context).size.height * 0.1,
                        child: IconButton(
                            onPressed: () {},
                            icon: Image.asset("assets/icons/tshirt.png", fit:BoxFit.fill)
                        ),
                      ),
                      Text("Одежда")
                    ],
                  ),
                  Column(
                    children: [
                      SizedBox(
                        width: MediaQuery.of(context).size.width * 0.2,
                        height: MediaQuery.of(context).size.height * 0.1,
                        child: IconButton(
                            onPressed: () {},
                            icon: Image.asset("assets/icons/drink.png", fit:BoxFit.fill)
                        ),
                      ),
                      Text("Металл")
                    ],
                  ),
                  Column(
                    children: [
                      SizedBox(
                        width: MediaQuery.of(context).size.width * 0.2,
                        height: MediaQuery.of(context).size.height * 0.1,
                        child: IconButton(
                            onPressed: () {},
                            icon: Image.asset("assets/icons/food.png", fit:BoxFit.fill)
                        ),
                      ),
                      Text("Бумага")
                    ],
                  ),
                  Column(
                    children: [
                      SizedBox(
                        width: MediaQuery.of(context).size.width * 0.2,
                        height: MediaQuery.of(context).size.height * 0.1,
                        child: IconButton(
                            onPressed: () {},
                            icon: Image.asset("assets/icons/biohazard.png", fit:BoxFit.fill)
                        ),
                      ),
                      Text("Химикаты")
                    ],
                  ),
                ]
            ),
            const Divider(
              height: 40,
              thickness: 1,
              color: Colors.black26,
            ),
            Image.asset(
              "assets/images/coffee.png",
              height: MediaQuery.of(context).size.height * 0.15,
              width: MediaQuery.of(context).size.width
            ),
            const Padding(padding: EdgeInsets.only(bottom: 20)),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Image.asset(
                  "assets/images/water.png",
                  width: MediaQuery.of(context).size.width * 0.45
                ),
                Image.asset(
                  "assets/images/hueta.png",
                  width: MediaQuery.of(context).size.width * 0.45
                ),
              ],
            )
          ],
        ),
      );
  }
}