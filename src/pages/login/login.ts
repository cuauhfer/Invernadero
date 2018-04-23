import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import {HomePage} from '../home/home';
import { Http } from "@angular/http";
import { AlertController} from 'ionic-angular';

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {
	usuario:string = "";
	password:string = "";
	home = HomePage;

  constructor(public navCtrl: NavController, public navParams: NavParams,
              private http: Http,
              private alerta: AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }

  clickBoton(){
  	console.log(this.usuario);
  	console.log(this.password);
  
    this.http.get('/login/?user=' + this.usuario + '&pwd=' + this.password).subscribe( data => {
      console.log("exito");
      console.log(data.text());

      if(data.text() == "True"){
        this.navCtrl.setRoot(this.home);
      }
      else{
        let a = this.alerta.create({
          title: "Error",
          subTitle: "Usuario o contraseña incorrectos",
          buttons: ["OK"]
        });
        a.present();
      }
    }, error =>{
      console.log("error");
      console.log(error);
    });
  }

}
