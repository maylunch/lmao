import 'package:flutter/material.dart';
import 'core/theme.dart';
import 'core/router.dart';

void main() {
  runApp(const LmaoApp());
}

class LmaoApp extends StatelessWidget {
  const LmaoApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'LMAO',
      theme: AppTheme.dark(),
      routerConfig: appRouter,
    );
  }
}