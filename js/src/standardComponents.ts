import { lazy } from 'react';
import { registerComponent } from 'viewFactory';

const BoxPage = lazy(() => import('./components/BoxPage'));
const ButtonComponent = lazy(() => import('./components/ButtonComponent'));
const ButtonBarComponent = lazy(() => import('./components/ButtonBarComponent'));
const ChartComponent = lazy(() => import('./components/ChartComponent'));
const DateSelectComponent = lazy(() => import('./components/DateSelectComponent'));
const ErrorComponent = lazy(() => import('./components/ErrorComponent'));
const ExpandoComponent = lazy(() => import('./components/ExpandoComponent'));
const FileUploadComponent = lazy(() => import('./components/FileUploadComponent'));
const FragmentComponent = lazy(() => import('./components/FragmentComponent'));
const ParagraphComponent = lazy(() => import('./components/ParagraphComponent'));
const SelectComponent = lazy(() => import('./components/SelectComponent'));
const SideBarPage = lazy(() => import('./components/SideBarPage'));
const TextFieldComponent = lazy(() => import('./components/TextFieldComponent'));


export const registerStandardComponents = () => {
    registerComponent('BoxPage', BoxPage);
    registerComponent('Button', ButtonComponent);
    registerComponent('ButtonBar', ButtonBarComponent);
    registerComponent('Chart', ChartComponent);
    registerComponent('DateSelect', DateSelectComponent);
    registerComponent('Error', ErrorComponent);
    registerComponent('Expando', ExpandoComponent);
    registerComponent('FileUpload', FileUploadComponent);
    registerComponent('Fragment', FragmentComponent);
    registerComponent('Paragraph', ParagraphComponent);
    registerComponent('Select', SelectComponent);
    registerComponent('SidebarPage', SideBarPage);
    registerComponent('TextField', TextFieldComponent);
}
