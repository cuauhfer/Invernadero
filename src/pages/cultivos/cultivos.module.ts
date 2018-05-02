import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { CultivosPage } from './cultivos';

@NgModule({
  declarations: [
    CultivosPage,
  ],
  imports: [
    IonicPageModule.forChild(CultivosPage),
  ],
})
export class CultivosPageModule {}
