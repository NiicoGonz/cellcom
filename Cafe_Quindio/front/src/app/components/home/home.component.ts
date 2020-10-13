import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
// tslint:disable-next-line: variable-name
img_logo = './assets/Recursos-Caffe/Logo_cafe.jpg';
  constructor() { }

  ngOnInit(): void {
  }

}
