import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ValorPage } from "../valor/valor";
import { Http } from "@angular/http";

/**
 * Generated class for the CultivosPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cultivos',
  templateUrl: 'cultivos.html',
})
export class CultivosPage {
	valorPage = ValorPage;
  invernadero: any;
  cultivos: any;

  constructor(public navCtrl: NavController, public navParams: NavParams, 
                                private http: Http){
              this.invernadero = this.navParams.get('invernadero');
              console.log(this.invernadero.id);
              this.getCultivo();
  }

  getCultivo(){
  this.http.get('/cultivos/?id=' + this.invernadero.id).subscribe(data => {
    console.log(data.json());
    this.cultivos = data.json();
  }, error1 =>{
    console.log(error1);
  });
  
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad CultivosPage');
  }

  cambiarValor(){
  	this.navCtrl.push(this.valorPage);
  }

}
