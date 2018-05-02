import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { NavParams } from 'ionic-angular';
import { Http } from "@angular/http";
import { CultivosPage } from "../cultivos/cultivos";

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
	cultivosPage = CultivosPage;

	usuario:string;
	password:string;
	invernaderos:any;

  constructor(public navCtrl: NavController, public navParams: NavParams,
  								private http: Http) {
  	console.log(this.navParams.get('user'));
  	console.log(this.navParams.get('pwd'));

  	this.usuario = this.navParams.get('user');
  	this.password = this.navParams.get('pwd');

  	this.getInvernadero();
  }

  getInvernadero(){
  this.http.post('/invernaderos/',{user: this.usuario, pwd: this.password}).subscribe(data => {
  	console.log(data.json());
  	this.invernaderos = data.json();
  }, error1 =>{
  	console.log(error1);
  });
  

  }

  cambiarCultivos(){
  	this.navCtrl.push(this.cultivosPage);
  }

}
