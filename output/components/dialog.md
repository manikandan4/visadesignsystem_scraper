# dialog

## Metadata
- **Version**: 0.0.1
- **Description**: Pop-up windows that overlay page content to facilitate user interactions or show important information.
- **Category**: components

## Example Sections
1. **Default Dialogs**
   - Description: 

## Examples
### Default dialog
- **Section**: Default Dialogs
- **URL**: components/dialog/default-dialog
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'dialog';

export const DefaultDialog = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open default dialog</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        id={id}
        ref={ref}
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>Default title</DialogHeader>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vPaddingTop={16}>
            <Button>Primary action</Button>
            <Button colorScheme="secondary">Secondary action</Button>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={() => ref.current?.close()} />
      </Dialog>
    </>
  );
};

```

### Error dialog
- **Section**: Default Dialogs
- **URL**: components/dialog/error-dialog
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  DialogIcon,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'error-dialog';

export const ErrorDialog = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open error dialog</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        id={id}
        messageType="error"
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
        ref={ref}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>
            <DialogIcon />
            Error title
          </DialogHeader>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vPaddingTop={16}>
            <Button>Primary action</Button>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={() => ref.current?.close()} />
      </Dialog>
    </>
  );
};

```

### Success dialog
- **Section**: Default Dialogs
- **URL**: components/dialog/success-dialog
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  DialogIcon,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'success-dialog';

export const SuccessDialog = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open success dialog</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        ref={ref}
        id={id}
        messageType="success"
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>
            <DialogIcon />
            Success title
          </DialogHeader>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vPaddingTop={16}>
            <Button>Primary action</Button>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={() => ref.current?.close()} />
      </Dialog>
    </>
  );
};

```

### Warning dialog
- **Section**: Default Dialogs
- **URL**: components/dialog/warning-dialog
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  DialogIcon,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'warning-dialog';

export const WarningDialog = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open warning dialog</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        ref={ref}
        id={id}
        messageType="warning"
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>
            <DialogIcon />
            Warning title
          </DialogHeader>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vPaddingTop={16}>
            <Button>Primary action</Button>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={() => ref.current?.close()} />
      </Dialog>
    </>
  );
};

```

### Dialog without close icon button
- **Section**: Default Dialogs
- **URL**: components/dialog/close-button-dialog
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogContent,
  DialogHeader,
  DialogIcon,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'no-close-dialog';

export const CloseButtonDialog = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open dialog without close icon</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        ref={ref}
        id={id}
        messageType="error"
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>
            <DialogIcon />
            Error title
          </DialogHeader>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vJustifyContent="end" vPaddingTop={16}>
            <Button onClick={() => ref.current?.close()}>Close</Button>
          </Utility>
        </DialogContent>
      </Dialog>
    </>
  );
};

```

### Touring tips dialog
- **Section**: Default Dialogs
- **URL**: components/dialog/touring-tips-dialog
- **Tags**: 
```tsx
import {
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'touring-tips-dialog';

export const TouringTipsDialog = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  const onCloseDialog = () => ref.current?.close();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open touring tips dialog</Button>
      <Dialog
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        ref={ref}
        id={id}
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
      >
        <DialogContent>
          <DialogHeader id={`${id}-title`}>Touring tips title</DialogHeader>
          <Utility vAlignItems="center" vFlex vFlexRow vGap={8} vPaddingBottom={8}>
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
              <rect width="36" height="36" rx="18" fill="#B3D7FF" fillOpacity="0.35" />
              <path
                d="M17.238 13.856C16.8327 13.856 16.3953 13.936 15.926 14.096C15.4567 14.256 15.03 14.496 14.646 14.816H14.502L14.614 13.136C15.0087 12.88 15.478 12.6827 16.022 12.544C16.566 12.4053 17.0727 12.336 17.542 12.336C18.7473 12.336 19.6913 12.5867 20.374 13.088C21.0673 13.5787 21.414 14.4427 21.414 15.68C21.414 16.256 21.3233 16.784 21.142 17.264C20.9713 17.7333 20.742 18.16 20.454 18.544C20.1767 18.928 19.8833 19.28 19.574 19.6C19.382 19.8133 19.126 20.0747 18.806 20.384C18.486 20.6827 18.1287 21.008 17.734 21.36C17.3393 21.712 16.9393 22.0533 16.534 22.384H21.67L21.526 24H14.406V22.576C15.0247 22.0213 15.5527 21.5467 15.99 21.152C16.438 20.7573 16.8327 20.3947 17.174 20.064C17.5153 19.7333 17.83 19.4027 18.118 19.072C18.502 18.6347 18.8167 18.1493 19.062 17.616C19.318 17.072 19.446 16.5013 19.446 15.904C19.446 15.1467 19.2593 14.6187 18.886 14.32C18.5127 14.0107 17.9633 13.856 17.238 13.856Z"
                fill="black"
              />
            </svg>
            <Typography variant="body-2-bold">Touring tips instructions</Typography>
          </Utility>
          <Typography id={`${id}-description`}>
            This is required text that describes the dialog title in more detail.
          </Typography>
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vJustifyContent="between" vPaddingTop={16}>
            <Typography>2 of 4</Typography>
            <Utility vFlex vFlexWrap vGap={8} vJustifyContent="between">
              <Button colorScheme="secondary" onClick={onCloseDialog}>
                Previous
              </Button>
              <Button onClick={onCloseDialog}>Next</Button>
            </Utility>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={onCloseDialog} />
      </Dialog>
    </>
  );
};

```

## Property Sections
### Dialog
- **Selector**: <Dialog />
- **Description**: Pop-up windows that overlay page content to facilitate user interactions or show important information.

### DialogCloseButton
- **Selector**: <DialogCloseButton />
- **Description**: Button that appears in dialog pop-up windows to close them.

### DialogHeader
- **Selector**: <DialogHeader />
- **Description**: Container for the heading area of a dialog pop-up window.

### MessageContent
- **Selector**: <MessageContent />
- **Description**: Container for message content elements.

### MessageIcon
- **Selector**: <MessageIcon />
- **Description**: Icon to display within message content.

### useFocusTrap
- **Selector**: None
- **Description**: This hook is used to trap focus inside a container.

## Properties
### messageType
- **Section**: Dialog
- **Type**: "subtle" , "warning" , "error" , "success"
- **Default**: 
- **Required**: false
- **Description**: Message Type

### ref
- **Section**: Dialog
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Dialog
- **Type**: ElementType
- **Default**: dialog
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: DialogCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: DialogCloseButton
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: DialogCloseButton
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: DialogCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: DialogCloseButton
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: DialogCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: DialogCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: DialogCloseButton
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: DialogCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: DialogCloseButton
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: DialogCloseButton
- **Type**: ElementType
- **Default**: 
- **Required**: false
- **Description**: Tag (not compatible with element property)

### colorScheme
- **Section**: DialogHeader
- **Type**: "default" , "subtle" , "active" , "on-active"
- **Default**: 
- **Required**: false
- **Description**: Color variant

### ref
- **Section**: DialogHeader
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: DialogHeader
- **Type**: ElementType
- **Default**: h2
- **Required**: false
- **Description**: Tag of Component

### ref
- **Section**: MessageContent
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: MessageContent
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### element
- **Section**: MessageIcon
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element

### ref
- **Section**: MessageIcon
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

