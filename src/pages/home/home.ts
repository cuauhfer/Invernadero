import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { CultivosPage } from "../cultivos/cultivos";

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
	cultivosPage = CultivosPage;

  constructor(public navCtrl: NavController) {

  }

  cambiarCultivos(){
  	this.navCtrl.push(this.cultivosPage);
  }

}
