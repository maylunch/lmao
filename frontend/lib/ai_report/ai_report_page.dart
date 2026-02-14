import 'package:flutter/material.dart';

class AIReportPage extends StatelessWidget {
  const AIReportPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('AI Report')),
      body: const Center(child: Text('Risk Score: 72')),
    );
  }
}