# Visa Design System Summary by Category

## Components

### footer

- **Description**: Content anchored at the bottom of a page to provide important information or links.
- **Details**: [details](components/footer.md)

**Example:**
```tsx
// If you are using Vite to run your application, please follow the instruction on the top of the page.
import { Footer, Link, Utility, VisaLogo } from '@visa/nova-react';

export const DefaultFooter = () => {
  return (
    <Footer className="v-gap-15">
      <Utility vFlex vMarginRight={1}>
        <VisaLogo aria-label="Visa" />
      </Utility>
      <Utility vFlex vFlexWrap vFlexGrow vJustifyContent="between" vGap={42}>
        {`Copyright © ${new Date().getFullYear()} Visa Inc. All Rights Reserved`}
        <Utility tag="ul" vFlex vFlexWrap vGap={16}>
          <li>
            <Link href="/footer">Contact us</Link>
          </li>
          <li>
            <Link href="/footer">Privacy</Link>
          </li>
          <li>
            <Link href="/footer">Legal/terms and conditions</Link>
          </li>
        </Utility>
      </Utility>
    </Footer>
  );
};
```

### input

- **Description**: Text fields that enable users to enter free-form content.
- **Details**: [details](components/input.md)

**Example:**
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'input-default';

export const DefaultInput = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input aria-required="true" id={id} type="text" />
      </InputContainer>
    </Utility>
  );
};
```

### accordion

- **Description**: Sets of vertical headers that reveal or hide the accordion panel.
- **Details**: [details](components/accordion.md)

**Example:**
```tsx
import { Accordion, AccordionHeading, AccordionPanel, AccordionToggleIcon, Typography } from '@visa/nova-react';

export const CollapsedAccordion = () => {
  return (
    <Accordion>
      <AccordionHeading buttonSize="large" colorScheme="secondary">
        <AccordionToggleIcon />
        Accordion title
      </AccordionHeading>
      <AccordionPanel>
        <Typography>This is required text that describes the accordion section in more detail.</Typography>
      </AccordionPanel>
    </Accordion>
  );
};
```

### radio

- **Description**: Interactive elements that allow users to select a single option from a list.
- **Details**: [details](components/radio.md)

**Example:**
```tsx
import { Label, Radio, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-radio';

export const DefaultRadio = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Radio id={id} name={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};
```

### content-card

- **Description**: Compact displays summarizing or directing users to more information.
- **Details**: [details](components/content-card.md)

**Example:**
```tsx
import { VisaChevronRightTiny } from '@visa/nova-icons-react';
import {
  Button,
  ContentCard,
  ContentCardBody,
  ContentCardSubtitle,
  ContentCardTitle,
  Link,
  Typography,
  Utility,
} from '@visa/nova-react';

export const DefaultContentCard = () => {
  return (
    <ContentCard>
      <Utility element={<ContentCardBody />} vFlex vFlexCol vGap={4}>
        <ContentCardTitle variant="headline-4">Headline</ContentCardTitle>
        <ContentCardSubtitle variant="subtitle-3">Subtitle</ContentCardSubtitle>
        <Typography className="v-pt-4">
          This is optional text that describes the headline and subtitle in more detail.
        </Typography>
        <Utility vAlignItems="center" vFlex vFlexWrap vGap={16} vPaddingTop={12}>
          <Button>Primary action</Button>
          <Link href="./content-card" noUnderline>
            Destination label <VisaChevronRightTiny rtl />
          </Link>
        </Utility>
      </Utility>
    </ContentCard>
  );
};
```

### wizard

- **Description**: Manages and navigates multi-step processes within your application.
- **Details**: [details](components/wizard.md)

**Example:**
```tsx
import {
  VisaArrowBackTiny,
  VisaArrowForwardTiny,
  VisaCheckmarkTiny,
  VisaChevronRightTiny,
  VisaEditTiny,
  VisaErrorAltTiny,
  VisaErrorTiny,
  VisaSuccessHigh,
} from '@visa/nova-icons-react';
import {
  Badge,
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  DialogIcon,
  Flag,
  FlagCloseButton,
  FlagContent,
  FlagIcon,
  Input,
  InputContainer,
  InputMessage,
  Label,
  Link,
  ScreenReader,
  Surface,
  Typography,
  Utility,
  UtilityFragment,
  Wizard,
  WizardStep,
  useFocusTrap,
  useWizard,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useState, useRef, ChangeEvent } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'horizontal-multi-page-wizard';
const navRegionAriaLabel = 'Horizontal multi-page wizard';

const steps = [
  {
    label: '1',
    title: 'Step 1 label',
    inputLabel: 'Label',
    inputId: `${id}-step-1-input`,
    buttonId: `${id}-step-1-button`,
  },
  {
    label: '2',
    title: 'Step 2 label',
    inputLabel: 'Label',
    inputId: `${id}-step-2-input`,
    buttonId: `${id}-step-2-button`,
  },
  {
    label: '3',
    title: 'Step 3 label',
    inputLabel: 'Label',
    inputId: `${id}-step-3-input`,
    buttonId: `${id}-step-3-button`,
  },
  {
    label: '4',
    title: 'Step 4 label',
    inputLabel: 'Label',
    inputId: `${id}-step-4-input`,
    buttonId: `${id}-step-4-button`,
  },
  {
    label: '5',
    title: 'Step 5 label',
  },
];

const exitDialogId = `${id}-exit-warning-dialog`;

const DEFAULT_INPUT_VALUES = Array(steps.length).fill('');

export const HorizontalWizard = () => {
  const {
    currentStep,
    isStepAvailable,
    isLastStep,
    isStepComplete,
    isStepError,
    onStepError,
    onStepChange,
    onStepComplete,
    onStepPrevious,
    onWizardReset,
  } = useWizard({ length: steps.length });

  // Track whether the wizard has been interacted with in order
  // to control focus within a useEffect
  const [hasWizardStepChanged, setHasWizardStepChanged] = useState(false);

  const { onKeyNavigation, ref: exitDialogRef } = useFocusTrap();

  const [inputValues, setInputValues] = useState(DEFAULT_INPUT_VALUES);

  const [showSavedFlag, setShowSavedFlag] = useState(false);
  const [formSubmitted, setFormSubmitted] = useState(false);

  // Create an array of refs to handle focusing input fields on error
  // https://react.dev/learn/manipulating-the-dom-with-refs#how-to-manage-a-list-of-refs-using-a-ref-callback
  const inputRefs = useRef(new Map());
  function getInputRefMap() {
    if (!inputRefs.current) {
      inputRefs.current = new Map();
    }
    return inputRefs.current;
  }

  const buttonRefs = useRef(new Map());
  function getButtonRefMap() {
    if (!buttonRefs.current) {
      buttonRefs.current = new Map();
    }
    return buttonRefs.current;
  }

  useEffect(() => {
    if (!hasWizardStepChanged) {
      return;
    }
    // apply focus if the currentStep has changed
    // (and the wizard has been interacted with)
    const buttonRefsMap = getButtonRefMap();
    const currentStepButtonNode = buttonRefsMap.get(steps[currentStep].buttonId);
    currentStepButtonNode.focus();
  }, [hasWizardStepChanged, currentStep]);

  const handleInputChange = (index: number, event: ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    const newInputValues = [...inputValues];
    newInputValues[index] = value;
    setInputValues(newInputValues);
  };

  // On next button click, simulate completion on all steps
  const handleClickNext = () => {
    if (!inputValues[currentStep]) {
      onStepError(currentStep);
      // find the input element with the error in the refs map and set focus on it
      const inputRefsMap = getInputRefMap();
      const currentStepInputNode = inputRefsMap.get(steps[currentStep].inputId);
      currentStepInputNode.focus();
      return;
    }

    setHasWizardStepChanged(true);
    setShowSavedFlag(false);
    onStepComplete(currentStep);
  };

  // On previous button click, reset the current step status from the list of completed steps
  const handleClickPrevious = () => {
    setHasWizardStepChanged(true);
    setShowSavedFlag(false);
    onStepPrevious();
  };

  const handleSave = () => {
    setShowSavedFlag(true);
  };

  // On next button click, simulate completion on all steps
  const handleResetWizard = () => {
    setHasWizardStepChanged(true);
    setInputValues(DEFAULT_INPUT_VALUES);
    setFormSubmitted(false);
    onWizardReset();
  };

  const handleSubmit = () => {
    const formValues: { [key: string]: string } = {};
    steps.forEach((step, i) => {
      if (!step.inputId) return;
      formValues[step.inputId] = inputValues[i];
    });
    setFormSubmitted(true);
  };

  const handleExit = () => {
    exitDialogRef.current?.showModal();
  };

  // On step button click, change the current step and reset the status of all steps after the clicked step
  const handleClickStep = (i: number) => {
    setHasWizardStepChanged(true);
    onStepChange(i);
  };

  const renderSummaryStep = () => (
    <Utility vAlignSelf="center" vFlex vFlexCol vGap={10} style={{ maxWidth: '610px', width: '100%' }}>
      <UtilityFragment
        vAlignSelf="center"
        vFlex
        vJustifyContent="center"
        vPaddingVertical={44}
        vPaddingHorizontal={32}
        vGap={32}
      >
        <Surface>
          <Utility style={{ maxWidth: '400px', width: '100%' }}>
            <Typography tag="h2" variant="headline-2">
              Summary
            </Typography>
            <ol>
              {steps.slice(0, steps.length - 1).map((step, i) => (
                <UtilityFragment
                  key={i}
                  vPaddingVertical={20}
                  style={{
                    borderBlockEnd: i < steps.length - 2 ? '1px solid rgba(0,0,0,0.10)' : 'none',
                  }}
                >
                  <li>
                    <Utility vFlex vJustifyContent="between">
                      <Typography
                        tag="h3"
                        variant="body-2-bold"
                        colorScheme="subtle"
                      >{`${i + 1}. ${step.title}`}</Typography>
                      <Button
                        aria-label={`Edit step ${i + 1}`}
                        colorScheme="tertiary"
                        iconButton
                        buttonSize="small"
                        onClick={() => handleClickStep(i)}
                      >
                        <VisaEditTiny rtl />
                      </Button>
                    </Utility>
                    <Typography>{`${step.inputLabel}: ${inputValues[i]}`}</Typography>
                  </li>
                </UtilityFragment>
              ))}
            </ol>
          </Utility>
        </Surface>
      </UtilityFragment>
      <Typography>Changes have been automatically saved.</Typography>
      {renderActionButtons()}
    </Utility>
  );

  const renderActionButtons = () => {
    return (
      <Utility vPaddingVertical={12}>
        <Utility vJustifyContent="between" vFlex vFlexWrap vColGap={24} vRowGap={16}>
          <Utility vJustifyContent="start" vFlex vFlexWrap vColGap={24} vRowGap={16}>
            <Button onClick={handleSave} colorScheme="secondary">
              Save
            </Button>
            <Button onClick={handleExit} colorScheme="tertiary">
              Exit
            </Button>
          </Utility>
          <Utility vJustifyContent="end" vFlex vFlexWrap vColGap={24} vRowGap={16}>
            <UtilityFragment vHide={currentStep === 0}>
              <Button onClick={handleClickPrevious} colorScheme="secondary">
                <VisaArrowBackTiny />
                Back
              </Button>
            </UtilityFragment>
            <UtilityFragment vHide={currentStep === steps.length - 1}>
              <Button onClick={handleClickNext}>
                Next
                <VisaArrowForwardTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment vHide={currentStep !== steps.length - 1}>
              <Button onClick={handleSubmit}>Submit</Button>
            </UtilityFragment>
          </Utility>
        </Utility>
      </Utility>
    );
  };

  if (formSubmitted) {
    return (
      <Utility vFlex vJustifyContent="center" vGap={12}>
        <UtilityFragment
          vFlex
          vJustifyContent="center"
          vPaddingVertical={44}
          vPaddingHorizontal={32}
          vGap={32}
          style={{ maxWidth: '676px' }}
        >
          <Surface>
            <Utility vFlex vFlexCol vGap={24} vAlignItems="center" style={{ maxWidth: '394px', width: '394px' }}>
              <Typography tag="h2" variant="headline-2">
                Success
              </Typography>
              <VisaSuccessHigh
                style={
                  {
                    '--v-icon-primary': 'var(--palette-messaging-graphics-positive)',
                    '--v-icon-secondary': 'var(--palette-messaging-graphics-positive)',
                  } as CSSProperties
                }
              />
              <Typography tag="p" variant="body-2">
                This is required text that describes the success message in more detail.
              </Typography>
              <Utility vAlignSelf="stretch" vFlex vJustifyContent="center" vGap={24}>
                <Link element={<button />} onClick={handleResetWizard}>
                  Reset wizard example
                </Link>
                <Link href="./wizard">Destination label</Link>
              </Utility>
            </Utility>
          </Surface>
        </UtilityFragment>
      </Utility>
    );
  }

  return (
    <Utility vFlex vFlexCol vGap={12}>
      {showSavedFlag && (
        <UtilityFragment vAlignSelf="end">
          <Flag messageType="success">
            <FlagIcon />
            <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
              <ScreenReader>success</ScreenReader>
              Your progress has been saved.
            </FlagContent>
            <FlagCloseButton onClick={() => setShowSavedFlag(false)} />
          </Flag>
        </UtilityFragment>
      )}
      <nav aria-label={navRegionAriaLabel}>
        <Wizard>
          {steps.map((step, i) => (
            <WizardStep key={`horizontal-wizard-step-${i + 1}`} aria-current={currentStep === i ? 'step' : undefined}>
              {isStepAvailable(i) ? (
                <>
                  <ScreenReader>
                    {`${isStepError(i) ? 'Error ' : isStepComplete(i) ? 'Completed ' : ''}Step ${i + 1} of ${steps.length}`}
                  </ScreenReader>
                  <Button
                    className={`${
                      currentStep === i ? 'v-typography-label-large-active' : 'v-typography-body-2'
                    } v-typography-color-default`}
                    colorScheme="tertiary"
                    onClick={() => handleClickStep(i)}
                    id={step.buttonId}
                    ref={node => {
                      const map = getButtonRefMap();
                      if (node) {
                        // store the node in the inputRefs Map
                        map.set(step.buttonId, node);
                      } else {
                        map.delete(step.buttonId);
                      }
                    }}
                  >
                    <Badge
                      aria-current={i === currentStep ? 'step' : undefined}
                      active={i === currentStep && !isStepError(i) && !isStepComplete(i)}
                      badgeType={isStepError(i) ? 'critical' : isStepComplete(i) ? 'stable' : 'subtle'}
                      badgeVariant="icon"
                      clear={i !== currentStep}
                      tag="span"
                    >
                      {isStepError(i) ? <VisaErrorAltTiny /> : isStepComplete(i) ? <VisaCheckmarkTiny /> : step.label}
                    </Badge>
                    <Typography>{step.title}</Typography>
                    {i < steps.length - 1 && <VisaChevronRightTiny className="v-typography-color-subtle" />}
                  </Button>
                </>
              ) : (
                <>
                  <ScreenReader>
                    {`${isStepError(i) ? 'Error ' : isStepComplete(i) ? 'Completed ' : ''}Step ${i + 1} of ${steps.length}`}
                  </ScreenReader>
                  <Badge
                    active={i === currentStep && !isStepError(i) && !isStepComplete(i)}
                    clear={i !== currentStep}
                    badgeType={isStepError(i) ? 'critical' : isStepComplete(i) ? 'stable' : 'subtle'}
                    badgeVariant="icon"
                    tag="span"
                  >
                    {isStepError(i) ? <VisaErrorAltTiny /> : isStepComplete(i) ? <VisaCheckmarkTiny /> : step.label}
                  </Badge>
                  <Typography variant={i === currentStep ? 'label-large-active' : 'body-2'}>{step.title}</Typography>
                  {!isLastStep(i) && <VisaChevronRightTiny className="v-typography-color-subtle" />}
                </>
              )}
            </WizardStep>
          ))}
        </Wizard>
      </nav>
      <Utility vFlex vFlexCol vGap={12}>
        {steps.slice(0, steps.length - 1).map((step, i) => {
          return (
            <Utility key={i} vFlex vFlexCol vGap={4} vHide={currentStep !== i}>
              <Label htmlFor={step.inputId}>{`${step.inputLabel} (required)`}</Label>
              <InputContainer>
                <Input
                  aria-describedby={`${step.inputId}-message`}
                  aria-required="true"
                  aria-invalid={isStepError(i)}
                  id={step.inputId}
                  type="text"
                  value={inputValues[i]}
                  onChange={e => handleInputChange(i, e as ChangeEvent<HTMLInputElement>)}
                  ref={node => {
                    const map = getInputRefMap();
                    if (node) {
                      // store the node in the inputRefs Map
                      map.set(step.inputId, node);
                    } else {
                      map.delete(step.inputId);
                    }
                  }}
                />
              </InputContainer>
              {isStepError(i) && (
                <InputMessage aria-atomic="true" aria-live="assertive" id={`${step.inputId}-message`} role="alert">
                  <VisaErrorTiny />
                  This is required text that describes the error in more detail.
                </InputMessage>
              )}
              {renderActionButtons()}
            </Utility>
          );
        })}
        {currentStep === steps.length - 1 && renderSummaryStep()}
      </Utility>
      <Dialog
        aria-describedby={`${exitDialogId}-description`}
        aria-labelledby={`${exitDialogId}-title`}
        ref={exitDialogRef}
        id={exitDialogId}
        messageType="warning"
        onKeyDown={e => onKeyNavigation(e, exitDialogRef.current?.open)}
        style={{ maxWidth: '300px' }}
      >
        <DialogContent>
          <DialogHeader id={`${exitDialogId}-title`}>
            <DialogIcon />
            Exit form?
          </DialogHeader>
          <Typography id={`${exitDialogId}-description`}>
            Your progress has been automatically saved. You can continue where you left off when you return.
          </Typography>
          <Utility vFlex vFlexWrap vGap={8} vPaddingTop={16}>
            <Button
              style={{ width: '100%' }}
              onClick={() => {
                window?.location?.reload();
              }}
            >
              Exit
            </Button>
          </Utility>
        </DialogContent>
        <DialogCloseButton onClick={() => exitDialogRef.current?.close()} />
      </Dialog>
    </Utility>
  );
};
```

### date-and-time-selectors

- **Description**: 
- **Details**: [details](components/date-and-time-selectors.md)

**Example:**
```tsx
import { Input, InputContainer, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-date-selector';

export const DefaultDateSelector = () => {
  return (
    <Utility vFlex vFlexCol vGap={4}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Input id={id} required type="date" />
      </InputContainer>
    </Utility>
  );
};
```

### button

- **Description**: Interactive elements enabling users to take actions within an interface.
- **Details**: [details](components/button.md)

**Example:**
```tsx
import { Button } from '@visa/nova-react';

export const DefaultButton = () => {
  return <Button>Primary action</Button>;
};
```

### banner

- **Description**: Messages indicating the global status of an application or website.
- **Details**: [details](components/banner.md)

**Example:**
```tsx
import { Banner } from '@visa/nova-react';

export const EmptyInformationBanner = () => {
  return <Banner></Banner>;
};
```

### surface

- **Description**: Styles container to be used for alternate backgrounds.
- **Details**: [details](components/surface.md)

**Example:**
```tsx
import { Surface } from '@visa/nova-react';

export const DefaultSurface = () => {
  return <Surface>Example</Surface>;
};
```

### listbox

- **Description**: Container that displays a list of items available for selection.
- **Details**: [details](components/listbox.md)

**Example:**
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, Radio } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-single-select-listbox';

const options = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E', 'Item F', 'Item G'];

export const DefaultSingleListbox = () => {
  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox id={id} scroll tag="div">
          {options.map((option, index) => (
            <ListboxItem htmlFor={`${id}-option-${index}`} key={`${id}-option-${index}`} tag="label">
              <Radio className="v-flex-shrink-0" id={`${id}-option-${index}`} name={`${id}-options`} />
              <Label tag="span">{option}</Label>
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};
```

### breadcrumbs

- **Description**: Supplemental navigation indicating the user's location in a site or app.
- **Details**: [details](components/breadcrumbs.md)

**Example:**
```tsx
import { Breadcrumbs, Link } from '@visa/nova-react';

export const DefaultBreadcrumbs = () => {
  return (
    <Breadcrumbs ariaLabel="Default breadcrumbs">
      <ol>
        <li>
          <Link href="./">L1 label</Link>
        </li>
        <li>
          <Link href="./">L2 label</Link>
        </li>
        <li>
          <Link href="./">L3 label</Link>
        </li>
        <li>
          <span aria-current="page">L4 label</span>
        </li>
      </ol>
    </Breadcrumbs>
  );
};
```

### checkbox

- **Description**: Interactive element enabling users to select one or more independent options from a group.
- **Details**: [details](components/checkbox.md)

**Example:**
```tsx
import { Checkbox, Label, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'checkbox-default';

export const DefaultCheckbox = () => {
  return (
    <Utility vAlignItems="center" vFlex vGap={2}>
      <Checkbox id={id} />
      <Label htmlFor={id}>Label</Label>
    </Utility>
  );
};
```

### horizontal-navigation

- **Description**: Menu or panel at the top of page content that links to important pages or features.
- **Details**: [details](components/horizontal-navigation.md)

**Example:**
```tsx
import {
  autoUpdate,
  offset,
  FloatingFocusManager,
  useClick,
  useFloating,
  useInteractions,
  useDismiss,
} from '@floating-ui/react';
import {
  VisaAccountLow,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaCloseLow,
  VisaCloseTiny,
  VisaMenuLow,
  VisaNotificationsLow,
  VisaSearchLow,
} from '@visa/nova-icons-react';
import {
  Avatar,
  Badge,
  Button,
  Divider,
  DropdownButton,
  DropdownMenu,
  Input,
  InputContainer,
  Link,
  Listbox,
  ListboxItem,
  Nav,
  NavAppName,
  Surface,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-horizontal-nav';

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './horizontal-navigation',
  },
];

const label3SubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-label-3-sub-item-0`,
    href: './horizontal-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-label-3-sub-item-1`,
    href: './horizontal-navigation',
  },
];

export const DefaultHorizontalNav = () => {
  const searchInputRef = useRef<HTMLInputElement | null>();
  const searchButtonRef = useRef<HTMLButtonElement | null>();

  const [accountMenuOpen, setAccountMenuOpen] = useState(false);
  const [mobileAccountMenuOpen, setMobileAccountMenuOpen] = useState(false);
  const [mobileLabel3MenuOpen, setMobileLabel3MenuOpen] = useState(false);
  const [expandSearch, setExpandSearch] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [label3Open, setLabel3Open] = useState(false);
  const searchInitiallyActivated = useRef(false);

  useEffect(() => {
    if (expandSearch && searchInitiallyActivated.current) {
      searchInputRef.current?.focus();
    }
    if (!expandSearch && searchInitiallyActivated.current) {
      searchButtonRef.current?.focus();
    }
  }, [expandSearch]);
  
  // For dropdown menus in the horizontal nav, we use floating UI for
  // -opening
  // -positioning
  // -dismissing

  // floating-ui setup for the account dropdown
  const {
    context: accountFloatingContext,
    floatingStyles: accountFloatingStyles,
    refs: accountFloatingRefs,
  } = useFloating({
    middleware: [offset(2)],
    open: accountMenuOpen,
    onOpenChange: setAccountMenuOpen,
    placement: 'bottom-end',
    whileElementsMounted: autoUpdate,
  });
  const clickAccountRef = useClick(accountFloatingContext);
  const dismissAccountMenu = useDismiss(accountFloatingContext);
  const { getReferenceProps: getAccountReferenceProps, getFloatingProps: getAccountFloatingProps } = useInteractions([
    clickAccountRef,
    dismissAccountMenu,
  ]);

  // floating-ui setup for the label3 tab dropdown
  const {
    context: label3FloatingContext,
    floatingStyles: label3FloatingStyles,
    refs: label3FloatingRefs,
  } = useFloating({
    middleware: [offset(8)],
    open: label3Open,
    onOpenChange: setLabel3Open,
    placement: 'bottom-start',
    whileElementsMounted: autoUpdate,
  });

  const clickLabel3Ref = useClick(label3FloatingContext);
  const dismissLabel3Menu = useDismiss(label3FloatingContext);
  const { getReferenceProps: getLabel3ReferenceProps, getFloatingProps: getLabel3FloatingProps } = useInteractions([
    clickLabel3Ref,
    dismissLabel3Menu,
  ]);

  const onToggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div>
      <Link skipLink href="#content">
        Skip to content
      </Link>
      <UtilityFragment vJustifyContent="between">
        <Nav id={id} orientation="horizontal" tag="header">
          {!expandSearch ? (
            <>
              <UtilityFragment vContainerHide="desktop">
                <DropdownButton
                  aria-controls={`${id}-mobile-menu`}
                  aria-expanded={mobileMenuOpen ? 'true' : 'false'}
                  aria-label="open menu"
                  aria-describedby={`${id}-mobile-menu-notifications-badge`}
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  id={`${id}-mobile-menu-button`}
                  onClick={onToggleMobileMenu}
                >
                  {mobileMenuOpen ? (
                    <VisaCloseTiny />
                  ) : (
                    <>
                      <VisaMenuLow />
                      <Badge
                        id={`${id}-mobile-menu-notifications-badge`}
                        aria-label="3 notifications"
                        badgeVariant="number"
                        tag="sup"
                      >
                        3
                      </Badge>
                    </>
                  )}
                </DropdownButton>
              </UtilityFragment>
              <UtilityFragment vFlex vGap={16}>
                <Link
                  aria-label="Visa Application Name Home"
                  href="./horizontal-navigation"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Utility
                      vContainerHide="xs"
                      element={<Typography variant="headline-3">Application Name</Typography>}
                    />
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <UtilityFragment vFlex vJustifyContent="end" vFlexGrow vMarginLeft="auto" vContainerHide="mobile">
                <nav aria-label="Label for horizontal default example">
                  <UtilityFragment vGap={4}>
                    <Tabs>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 1</a>}
                        />
                      </Tab>
                      <Tab>
                        <Button
                          buttonSize="large"
                          colorScheme="tertiary"
                          element={<a href="./horizontal-navigation">L1 label 2</a>}
                        />
                      </Tab>
                      <Tab>
                        <DropdownButton
                          aria-expanded={label3Open}
                          aria-controls={label3Open ? `${id}-label-dropdown-menu` : undefined}
                          id={`${id}-label-dropdown-button`}
                          buttonSize="large"
                          colorScheme="tertiary"
                          ref={label3FloatingRefs.setReference}
                          {...getLabel3ReferenceProps()}
                        >
                          L1 label 3<TabSuffix element={label3Open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                        </DropdownButton>

                        {label3Open && (
                          <FloatingFocusManager
                            context={label3FloatingContext}
                            modal={false}
                            initialFocus={-1}
                            restoreFocus={true}
                          >
                            <DropdownMenu
                              id={`${id}-label-dropdown-menu`}
                              aria-hidden={!label3Open}
                              style={
                                {
                                  inlineSize: '180px',
                                  position: 'absolute',
                                  ...label3FloatingStyles,
                                  zIndex: 1,
                                } as CSSProperties
                              }
                              ref={label3FloatingRefs.setFloating}
                              {...getLabel3FloatingProps()}
                            >
                              <Listbox>
                                {label3SubItems.map(label3SubItem => (
                                  <li key={label3SubItem.id}>
                                    <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                      <ListboxItem href={label3SubItem.href} tag="a">
                                        {label3SubItem.tabLabel}
                                      </ListboxItem>
                                    </UtilityFragment>
                                  </li>
                                ))}
                              </Listbox>
                            </DropdownMenu>
                          </FloatingFocusManager>
                        )}
                      </Tab>
                    </Tabs>
                  </UtilityFragment>
                </nav>
              </UtilityFragment>
              <Utility vFlex vGap={8} vMarginLeft={8}>
                <Button
                  aria-label="search site"
                  buttonSize="large"
                  ref={searchButtonRef}
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => { setExpandSearch(true); searchInitiallyActivated.current = true; }}

                >
                  <VisaSearchLow />
                </Button>
                <UtilityFragment vContainerHide="mobile">
                  <Button
                    aria-label="notifications"
                    aria-describedby={`${id}-notifications-badge`}
                    buttonSize="large"
                    colorScheme="tertiary"
                    iconButton
                  >
                    <VisaNotificationsLow />

                    <Badge id={`${id}-notifications-badge`} badgeVariant="number" tag="sup">
                      3
                    </Badge>
                  </Button>
                </UtilityFragment>
                <UtilityFragment vContainerHide="mobile">
                  <Tab tag="div">
                    <DropdownButton
                      aria-expanded={accountMenuOpen}
                      aria-controls={accountMenuOpen ? `${id}-account-menu` : undefined}
                      aria-label="Alex Miller"
                      buttonSize="large"
                      colorScheme="tertiary"
                      element={<Avatar tag="button" />}
                      ref={accountFloatingRefs.setReference}
                      {...getAccountReferenceProps()}
                    >
                      <VisaAccountLow />
                      <TabSuffix element={accountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                    </DropdownButton>
                    {accountMenuOpen && (
                      <FloatingFocusManager
                        context={accountFloatingContext}
                        modal={false}
                        initialFocus={-1}
                        restoreFocus={true}
                      >
                        <DropdownMenu
                          id={`${id}-account-menu`}
                          aria-hidden={!accountMenuOpen}
                          style={
                            {
                              inlineSize: '180px',
                              position: 'absolute',
                              ...accountFloatingStyles,
                              zIndex: 1,
                            } as CSSProperties
                          }
                          ref={accountFloatingRefs.setFloating}
                          {...getAccountFloatingProps()}
                        >
                          <Listbox>
                            {accountSubItems.map(accountSubItem => (
                              <UtilityFragment key={accountSubItem.id}>
                                <li>
                                  <UtilityFragment vPaddingVertical={4} vPaddingHorizontal={8}>
                                    <ListboxItem href={accountSubItem.href} tag="a">
                                      {accountSubItem.tabLabel}
                                    </ListboxItem>
                                  </UtilityFragment>
                                </li>
                              </UtilityFragment>
                            ))}
                          </Listbox>
                        </DropdownMenu>
                      </FloatingFocusManager>
                    )}
                  </Tab>
                </UtilityFragment>
              </Utility>
            </>
          ) : (
            <UtilityFragment vFlex>
              <Surface
                style={
                  {
                    '--v-surface-background': 'var(--palette-default-surface-3)',
                    '--v-surface-border-radius': 'var(--size-rounded-medium)',
                    '--v-surface-padding-inline': 'var(--size-scalable-8)',
                  } as CSSProperties
                }
              >
                <InputContainer>
                  <VisaSearchLow />
                  <Input
                    id={`${id}-search-field`}
                    name={`${id}-search-field`}
                    ref={searchInputRef}
                    required
                    type="search"
                    aria-label="Search"
                    placeholder="Search"
                  />
                </InputContainer>
                <Button
                  aria-label="close search"
                  buttonSize="large"
                  colorScheme="tertiary"
                  iconButton
                  onClick={() => setExpandSearch(false)}
                >
                  <VisaCloseLow />
                </Button>
              </Surface>
            </UtilityFragment>
          )}
        </Nav>
      </UtilityFragment>
      <UtilityFragment vContainerHide="desktop" vHide={!mobileMenuOpen}>
        <Nav
          aria-label="Label for horizontal default example"
          aria-hidden={!mobileMenuOpen}
          id={`${id}-mobile-menu`}
          orientation="vertical"
        >
          <Tabs orientation="vertical">
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 1</a>}
              />
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                element={<a href="./horizontal-navigation">L1 label 2</a>}
              />
            </Tab>
            <Tab>
              <Button
                aria-expanded={mobileLabel3MenuOpen}
                aria-controls={mobileLabel3MenuOpen ? `${id}-account-sub-menu` : 'undefined'}
                id={`${id}-mobile-menu-label-dropdown-button`}
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileLabel3MenuOpen(!mobileLabel3MenuOpen)}
              >
                L1 Label 3
                <TabSuffix element={mobileLabel3MenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>

              {mobileLabel3MenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {label3SubItems.map(label3SubItem => (
                    <Tab key={label3SubItem.id} id={label3SubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={label3SubItem.href}>{label3SubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
            <Tab>
              <Button
                buttonSize="large"
                colorScheme="tertiary"
                style={{ wordBreak: 'break-word', blockSize: 'max-content' } as CSSProperties}
              >
                Notifications
                <Badge badgeVariant="number" style={{ position: 'relative' }} tag="sup">
                  3
                </Badge>
              </Button>
            </Tab>
            <Divider dividerType="decorative"></Divider>
            <Tab tag="div">
              <Button
                aria-expanded={mobileAccountMenuOpen}
                aria-controls={`${id}-account-sub-menu`}
                aria-label="Alex Miller"
                buttonSize="large"
                colorScheme="tertiary"
                onClick={() => setMobileAccountMenuOpen(!mobileAccountMenuOpen)}
              >
                <VisaAccountLow />
                Alex Miller
                <TabSuffix element={mobileAccountMenuOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
              </Button>
              {mobileAccountMenuOpen && (
                <Tabs orientation="vertical" id={`${id}-account-sub-menu`}>
                  {accountSubItems.map(accountSubItem => (
                    <Tab key={accountSubItem.id} id={accountSubItem.id}>
                      <Button
                        colorScheme="tertiary"
                        element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                      />
                    </Tab>
                  ))}
                </Tabs>
              )}
            </Tab>
          </Tabs>
        </Nav>
      </UtilityFragment>
    </div>
  );
};
```

### pagination

- **Description**: Set of links used to navigate content split across multiple pages.
- **Details**: [details](components/pagination.md)

**Example:**
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import { Button, Pagination, PaginationOverflow } from '@visa/nova-react';

export const OneDigitPagination = () => {
  return (
    <nav aria-label="1 digit pagination" role="navigation">
      <Pagination className="v-flex v-flex-row v-align-items-center v-gap-4">
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to first page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaArrowStartTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-label="Go to previous page" buttonSize="small" colorScheme="tertiary" disabled iconButton>
            <VisaChevronLeftTiny rtl />
          </Button>
        </li>
        <li>
          <Button aria-current="true" aria-label="Page 1" colorScheme="tertiary">
            1
          </Button>
        </li>
        <li>
          <Button aria-label="Page 2" colorScheme="tertiary">
            2
          </Button>
        </li>
        <li>
          <Button aria-label="Page 3" colorScheme="tertiary">
            3
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 4" colorScheme="tertiary">
            4
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 5" colorScheme="tertiary">
            5
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 6" colorScheme="tertiary">
            6
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 7" colorScheme="tertiary">
            7
          </Button>
        </li>
        <PaginationOverflow className="v-flex v-align-items-center v-mobile-container-hide">
          <VisaOptionHorizontalTiny />
        </PaginationOverflow>
        <li className="v-mobile-container-hide">
          <Button aria-label="Page 100" colorScheme="tertiary">
            100
          </Button>
        </li>
        <li>
          <Button aria-label="Go to next page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaChevronRightTiny rtl />
          </Button>
        </li>
        <li className="v-mobile-container-hide">
          <Button aria-label="Go to last page" buttonSize="small" colorScheme="tertiary" iconButton>
            <VisaArrowEndTiny rtl />
          </Button>
        </li>
      </Pagination>
    </nav>
  );
};
```

### progress

- **Description**: Visual representation of the status of a system process.
- **Details**: [details](components/progress.md)

**Example:**
```tsx
import { VisaMediaPauseAltTiny, VisaMediaPlayAltTiny } from '@visa/nova-icons-react';
import { Button, ProgressLabel, ProgressLinear, Utility, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'indeterminate-linear-progress';

export const IndeterminateProgress = () => {
  const [paused, setPaused] = useState(false);
  const [initiated, setInitiated] = useState(false);
  const [loadingMsg, setLoadingMsg] = useState('');

const start = () => {
  setInitiated(true);
  setTimeout(() => {
    setLoadingMsg('Loading...');
  }, 0);
}
  
const reset = () => {
  setInitiated(false);
  setLoadingMsg('');
}

  return (
    <Utility vFlexCol vGap={12}>
        {initiated && (
      <Utility vFlexGrow>
        <UtilityFragment vMarginVertical={8}>
          <ProgressLinear id={id} paused={paused} />
        </UtilityFragment>
        <ProgressLabel htmlFor={id}>
          <Utility tag="span" role="alert">{loadingMsg}</Utility>
        </ProgressLabel>
      </Utility>
        )}
      <Utility vMarginVertical={12} vFlex vGap={12}>
        <Button onClick={() => start()}>
          Start
        </Button>
        <Button colorScheme="secondary" onClick={() => reset()}>
          Reset
        </Button>
        <Button colorScheme="secondary" onClick={() => setPaused(!paused)}>
          {paused ? (
            <>
              <VisaMediaPlayAltTiny />
              Play
            </>
          ) : (
            <>
              <VisaMediaPauseAltTiny />
              Pause
            </>
          )}
        </Button>
      </Utility>
    </Utility>
  );
};
```

### select

- **Description**: HTML element that allows users to select one option from a list.
- **Details**: [details](components/select.md)

**Example:**
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import { InputContainer, InputControl, Label, Select, Utility } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-select';

const options = ['Option A', 'Option B', 'Option C', 'Option D', 'Option E'];

export const DefaultSelect = () => {
  return (
    <Utility tag="fieldset" vFlex vFlexCol vGap={6}>
      <Label htmlFor={id}>Label (required)</Label>
      <InputContainer>
        <Select id={id} name={`${id}-name`}>
          <option hidden value="" />
          {options.map((option, index) => (
            <option key={`${id}-option-${index}`} value={index}>
              {option}
            </option>
          ))}
        </Select>
        <InputControl>
          <VisaChevronDownTiny />
        </InputControl>
      </InputContainer>
    </Utility>
  );
};
```

### table

- **Description**: Grid that organizes information, enabling data interaction, manipulation, and criteria-based analysis using columns and rows.
- **Details**: [details](components/table.md)

**Example:**
```tsx
import { ScreenReader, Table, Tbody, Td, Th, Thead, Tr } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const LargePaddingBandedTable = () => {
  return (
    <Table
      alternate
      style={
        {
          '--v-table-data-padding-block-default': 'var(--v-table-data-padding-block-large)',
          '--v-table-data-block-default': 'var(--v-table-data-block-large)',
        } as CSSProperties
      }
    >
      <ScreenReader tag="caption">Table with large padding and banded rows.</ScreenReader>
      <Thead>
        <Tr>
          <Th scope="col">Column A</Th>
          <Th scope="col">Column B</Th>
          <Th scope="col">Column C</Th>
          <Th scope="col">Column D</Th>
        </Tr>
      </Thead>
      <Tbody>
        <Tr>
          <Td>A1</Td>
          <Td>B1</Td>
          <Td>C1</Td>
          <Td>D1</Td>
        </Tr>
        <Tr>
          <Td>A2</Td>
          <Td>B2</Td>
          <Td>C2</Td>
          <Td>D2</Td>
        </Tr>
        <Tr>
          <Td>A3</Td>
          <Td>B3</Td>
          <Td>C3</Td>
          <Td>D3</Td>
        </Tr>
      </Tbody>
    </Table>
  );
};
```

### panel

- **Description**: Collapsible or persistent containers used to present supplementary information.
- **Details**: [details](components/panel.md)

**Example:**
```tsx
import { VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Panel,
  PanelBody,
  PanelContent,
  PanelHeader,
  Typography,
  useFocusTrap,
  Utility,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'modal-panel-default';

export const ModalPanel = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open modal panel</Button>
      <Panel
        aria-describedby={`${id}-description`}
        aria-labelledby={`${id}-title`}
        aria-modal="true"
        id={id}
        onKeyDown={e => onKeyNavigation(e, ref.current?.open)}
        ref={ref}
        tag="dialog"
      >
        <PanelContent>
          <Utility element={<PanelHeader />} vFlex vFlexRow vJustifyContent="between" vGap={4}>
            <Typography id={`${id}-title`} tag="h2" variant="headline-3">
              Panel title
            </Typography>
            <Button
              aria-label="Close panel"
              buttonSize="small"
              className="-v-mt-3 -v-mr-8"
              colorScheme="tertiary"
              iconButton
              onClick={() => ref.current?.close()}
              subtle
            >
              <VisaCloseTiny />
            </Button>
          </Utility>
          <PanelBody>
            <Typography id={`${id}-description`} tag="h3" variant="subtitle-2">
              Panel subtitle
            </Typography>
            <Typography>
              This is required text that can be used to describe the panel title and subtitle in more detail.
            </Typography>
          </PanelBody>
        </PanelContent>
      </Panel>
    </>
  );
};
```

### vertical-navigation

- **Description**: Menu or panel next to the page content that links to important pages or features.
- **Details**: [details](components/vertical-navigation.md)

**Example:**
```tsx
import {
  VisaAccountTiny,
  VisaChevronDownTiny,
  VisaChevronUpTiny,
  VisaMediaFastForwardTiny,
  VisaMediaRewindTiny,
} from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { useState } from 'react';
import Styles from './styles.module.scss';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-vertical-navigation';
const navRegionAriaLabel = 'Default vertical navigation';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './vertical-navigation',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './vertical-navigation',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './vertical-navigation',
  },
];

/*
 * Styles for the application container and main content
 * -----------------------------------------------------
 * .appContainer {
 *   &:global(:has(.v-nav .v-tabs)) {
 *     // The open navigation should be 242px
 *     grid-template-columns: 242px 1fr;
 *   }
 * }
 *
 * .layoutContainer {
 *   min-block-size: 700px;
 *   display: grid;
 *   grid-template-columns: auto 1fr;
 * }
 *
 * .mainContent {
 *   background-color: whitesmoke;
 *   min-block-size: 300px;
 *   padding: 12px;
 * }
 */

export const DefaultVerticalNavigation = () => {
  const [navExpanded, setNavExpanded] = useState(true);
  const [accountTabOpen, setAccountTabOpen] = useState(false);

  return (
    <div className={Styles.appContainer}>
      <div id="layout" className={Styles.layoutContainer}>
        <Nav id={id} orientation="vertical" tag="header">
          {navExpanded && (
            <Link skipLink href="#content">
              Skip to content
            </Link>
          )}
          {navExpanded && (
            <>
              <UtilityFragment
                vFlex
                vFlexCol
                vGap={12}
                vMarginTop={16}
                vMarginRight={16}
                vMarginBottom={30}
                vMarginLeft={20}
              >
                <Link
                  aria-label="Visa Application Name Home"
                  href="https://www.visa.com"
                  id={`${id}-home-link`}
                  noUnderline
                  style={{ backgroundColor: 'transparent' }}
                >
                  <VisaLogo />
                  <NavAppName>
                    <Typography variant="subtitle-1">Application Name</Typography>
                  </NavAppName>
                </Link>
              </UtilityFragment>
              <nav aria-label={navRegionAriaLabel}>
                <UtilityFragment vGap={8}>
                  <Tabs orientation="vertical">
                    {tabsContent.map(tabContent => (
                      <Tab key={tabContent.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href="./vertical-navigation">{tabContent.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </nav>
            </>
          )}
          <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
            {navExpanded && (
              <>
                <Divider dividerType="decorative" />
                <Tab tag="div">
                  <Button
                    aria-expanded={accountTabOpen}
                    aria-controls={`${id}-account-sub-menu`}
                    aria-label="Alex Miller"
                    buttonSize="large"
                    colorScheme="tertiary"
                    onClick={() => setAccountTabOpen(!accountTabOpen)}
                  >
                    <VisaAccountTiny />
                    Alex Miller
                    <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                  </Button>
                  <UtilityFragment vHide={!accountTabOpen}>
                    <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                      {accountSubItems.map(accountSubItem => (
                        <Tab key={accountSubItem.id} id={accountSubItem.id}>
                          <Button
                            colorScheme="tertiary"
                            element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                          />
                        </Tab>
                      ))}
                    </Tabs>
                  </UtilityFragment>
                </Tab>
              </>
            )}
            <UtilityFragment vMarginLeft={navExpanded ? 'auto' : 5} vMarginRight={navExpanded ? 8 : 5}>
              <Button
                aria-label="Side bar"
                aria-expanded={!!navExpanded}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => setNavExpanded(!navExpanded)}
                subtle
              >
                {navExpanded ? <VisaMediaRewindTiny rtl /> : <VisaMediaFastForwardTiny rtl />}
              </Button>
            </UtilityFragment>
          </Utility>
        </Nav>
        <div className={Styles.mainContent}>
          <Typography>Main Content</Typography>
        </div>
      </div>
    </div>
  );
};
```

### dialog

- **Description**: Pop-up windows that overlay page content to facilitate user interactions or show important information.
- **Details**: [details](components/dialog.md)

**Example:**
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

### tabs

- **Description**: Organizational element that separates content and allows users to switch between views.
- **Details**: [details](components/tabs.md)

**Example:**
```tsx
import { Button, Surface, Tab, Tabs, Utility, UtilityFragment, useTabs } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'nova-vertical-tabs-example';

const tabsContent = [
  {
    tabLabel: 'Label 1',
    text: `This is the content area for label 1`,
    id: `${id}-tab-0`,
  },
  {
    tabLabel: 'Label 2',
    text: `This is the content area for label 2`,
    id: `${id}-tab-1`,
  },
  {
    tabLabel: 'Label 3',
    text: `This is the content area for label 3`,
    id: `${id}-tab-2`,
  },
  {
    tabLabel: 'Label 4',
    text: `This is the content area for label 4`,
    id: `${id}-tab-3`,
  },
];

export const DefaultVerticalTabs = () => {
  const {
    getTabIndex,
    onIndexChange,
    onKeyNavigation,
    ref: tabsRef,
    selectedIndex,
  } = useTabs({ arrowKeyNavigation: 'vertical', defaultSelected: 0 });

  return (
    <Utility vFlex vFlexWrap vGap={8}>
      <Tabs onKeyDown={onKeyNavigation} orientation="vertical" role="tablist" style={{ flexBasis: '30%' }}>
        {tabsContent.map((tabContent, index) => (
          <Tab key={tabContent.id} role="none">
            <Button
              aria-selected={index === selectedIndex}
              aria-controls={tabContent.id}
              colorScheme="tertiary"
              onClick={() => onIndexChange(index)}
              ref={el => {
                tabsRef.current[index] = el;
              }}
              role="tab"
              tabIndex={getTabIndex(index)}
            >
              {tabContent.tabLabel}
            </Button>
          </Tab>
        ))}
      </Tabs>
      <Utility vFlex vFlexGrow vElevation="inset">
        <UtilityFragment vPadding={10}>
          <Surface id={tabsContent[selectedIndex].id} role="tabpanel">
            <span>{tabsContent[selectedIndex]?.text}</span>
          </Surface>
        </UtilityFragment>
      </Utility>
    </Utility>
  );
};
```

### toggle

- **Description**: Selection element that allows users to switch between states or views.
- **Details**: [details](components/toggle.md)

**Example:**
```tsx
import { Toggle, ToggleContainer, UtilityFragment } from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-toggle';

const options = [
  { label: 'Label 1', id: `${id}-label-1`, defaultSelected: true },
  { label: 'Label 2', id: `${id}-label-2` },
  { label: 'Label 3', id: `${id}-label-3` },
];

export const DefaultToggles = () => {
  const [togglePressedState, setTogglePressedState] = useState(options.map(o => !!o.defaultSelected));

  const handleSingleSelectTogglePress = (pressedIndex: number) => {
    setTogglePressedState(options.map((_, buttonIndex) => pressedIndex === buttonIndex));
  };

  return (
    <ToggleContainer>
      {options.map((option, optionIndex) => (
        <UtilityFragment key={option.id} vGap={6}>
          <Toggle
            tag="button"
            aria-pressed={togglePressedState[optionIndex]}
            onClick={() => handleSingleSelectTogglePress(optionIndex)}
          >
            {option.label}
          </Toggle>
        </UtilityFragment>
      ))}
    </ToggleContainer>
  );
};
```

### icon

- **Description**: Meant for use with sprites only. Uses dom href linking of sprite elements expected to already be in the DOM to render the icon.
- **Details**: [details](components/icon.md)

**Example:**
```tsx
import { VisaGlobalLow } from '@visa/nova-icons-react';

export const DefaultIcon = () => {
  return <VisaGlobalLow aria-hidden="false" aria-label="global" />;
};
```

### link

- **Description**: Text-based navigation elements that directs users to another destination.
- **Details**: [details](components/link.md)

**Example:**
```tsx
import { Link } from '@visa/nova-react';

export const DefaultLink = () => {
  return <Link href="./link">Destination label</Link>;
};
```

### color-selector

- **Description**: 
- **Details**: [details](components/color-selector.md)

**Example:**
```tsx
import {
  offset,
  safePolygon,
  useDismiss,
  useFloating,
  useFocus,
  useHover,
  useInteractions,
  useRole,
} from '@floating-ui/react';
import { Input, Label, Button, Tooltip, Utility, UtilityFragment } from '@visa/nova-react';
import { VisaAccessibilityTiny } from '@visa/nova-icons-react';
import { useState } from 'react';


// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'color-input';

export const ColorInput = () => {
  const [isOpen, setIsOpen] = useState(false);

  const { x, y, strategy, refs, context } = useFloating({
    middleware: [offset(2)],
    open: isOpen,
    onOpenChange: setIsOpen,
    placement: 'right',
  });

  const dismiss = useDismiss(context);
  const focus = useFocus(context);
  const hover = useHover(context, { handleClose: safePolygon(), move: false });
  const role = useRole(context, { role: 'tooltip' });

  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss, focus, hover, role]);

  return (
    <Utility vFlex vAlignItems="center" vGap={6}>
      <UtilityFragment vFlexGrow0 style={{ flexBasis: '5%' }}>
        <Input id={id} type="color" />
      </UtilityFragment>
      <Label htmlFor={id}>Label</Label>
      <Utility vAlignItems="center" vFlex vFlexCol vGap={2}>
      <Button 
        aria-labelledby={`${id}-label`}
        aria-label="Color selector accessibility information"
        colorScheme="tertiary"
        iconButton
        ref={refs.setReference} {...getReferenceProps()}>
          <VisaAccessibilityTiny rtl />
        </Button>
        {isOpen && (
        <Tooltip
          ref={refs.setFloating}
          style={{
            left: x,
            position: strategy,
            top: y,
            width: 'fit-content',
          }}
          {...getFloatingProps()}
        >
          For RGB, use values between 0-255. For HSL, use H values between 0-359, S and L values between 0-100%. For hex,
          use the format #RRGGBB and values between 0-9 or A-F.
        </Tooltip>
      )}
      </Utility>
    </Utility>
  );
};
```

### flag

- **Description**: Messages that provide low-priority updates about a process or event
- **Details**: [details](components/flag.md)

**Example:**
```tsx
import { Flag } from '@visa/nova-react';

export const EmptyInformationFlag = () => {
  return <Flag />;
};
```

### textarea

- **Description**: Input component with optional dynamic sizing, usually used for long-form text input.
- **Details**: [details](components/textarea.md)

### combobox

- **Description**: Dropdown menu enabling users to enter text or select items from a list.
- **Details**: [details](components/combobox.md)

**Example:**
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Button,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Radio,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox } from 'downshift';

type Item = { value: string };

const items: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const stateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) =>
  // this prevents on mouse hover, the item in the list is automatic selected
  type === useCombobox.stateChangeTypes.ItemMouseMove || type === useCombobox.stateChangeTypes.MenuMouseLeave
    ? {
        ...changes, // default Downshift new state changes on item selection.
        highlightedIndex: state.highlightedIndex,
      }
    : changes;

export const NoAutocompleteCombobox = () => {
  const {
    getInputProps,
    getItemProps,
    getLabelProps,
    getMenuProps,
    getToggleButtonProps,
    highlightedIndex,
    inputValue,
    isOpen,
  } = useCombobox({
    items: items,
    itemToString,
    stateReducer,
  });
  const { id: listboxId, ...listboxProps } = getMenuProps();

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label</Label>
          <UtilityFragment vFlexRow>
            <InputContainer>
              <Input
                aria-haspopup="listbox"
                name="text-input-field-1"
                type="text"
                {...getInputProps({ 'aria-expanded': isOpen, 'aria-owns': listboxId })}
              />
              <Button
                aria-label="expand"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                <VisaChevronDownTiny />
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <Listbox id={listboxId} {...listboxProps}>
          {items.map((item, index) => (
            <ListboxItem
              className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
              key={`no-autocomplete-example-${index}`}
              {...getItemProps({
                'aria-selected': inputValue === item.value,
                index,
                item,
              })}
            >
              <UtilityFragment vFlexShrink0>
                <Radio tag="span" />
              </UtilityFragment>
              {item.value}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </Combobox>
  );
};
```

### typography

- **Description**: Styles text in a consistent manner.
- **Details**: [details](components/typography.md)

**Example:**
```tsx
import { Typography } from '@visa/nova-react';

export const DisplayOneTypography = () => {
  return <Typography variant="display-1">The quick brown fox jumps over the lazy dog.</Typography>;
};
```

### switch

- **Description**: Binary control that allows users to toggle between two states, such as on/off.
- **Details**: [details](components/switch.md)

**Example:**
```tsx
import { Switch, SwitchLabel, Utility } from '@visa/nova-react';

const id = 'default-switch-example';

export const DefaultSwitch = () => {
  return (
    <Utility vFlex vFlexWrap vGap={10} vJustifyContent="between" vMargin={8} style={{ maxInlineSize: '288px' }}>
      <SwitchLabel htmlFor={`${id}-switch`}>Label</SwitchLabel>
      <Switch id={`${id}-switch`} name="default-switch" />
    </Utility>
  );
};
```

### avatar

- **Description**: Icons and/or text representing users or entities.
- **Details**: [details](components/avatar.md)

**Example:**
```tsx
import { Avatar } from '@visa/nova-react';

/// This is the base url for where your site is deployed. `import.meta.env.BASE_URL` is the environment variable used to import the base url for Vite. Change this import to match your build tool's base url.
const BASE_URL = import.meta.env.BASE_URL;
const user = 'Alex Miller';

export const SmallImageAvatar = () => {
  return <Avatar alt={user} small tag="img" src={BASE_URL + '/alex-miller-stock.png'} />;
};
```

### section-message

- **Description**: Section-level messages providing information about the status of a page or action.
- **Details**: [details](components/section-message.md)

**Example:**
```tsx
import { SectionMessage } from '@visa/nova-react';

export const EmptyInformationSectionMessage = () => {
  return <SectionMessage />;
};
```

### tooltip

- **Description**: Short message communicating the function or context of a control or object.
- **Details**: [details](components/tooltip.md)

**Example:**
```tsx
import {
  offset,
  safePolygon,
  useDismiss,
  useFloating,
  useFocus,
  useHover,
  useInteractions,
  useRole,
} from '@floating-ui/react';
import { Button, Tooltip, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const TopTooltip = () => {
  const [isOpen, setIsOpen] = useState(false);

  const { x, y, strategy, refs, context } = useFloating({
    middleware: [offset(2)],
    open: isOpen,
    onOpenChange: setIsOpen,
    placement: 'top',
  });

  const dismiss = useDismiss(context);
  const focus = useFocus(context);
  const hover = useHover(context, { handleClose: safePolygon(), move: false });
  const role = useRole(context, { role: 'tooltip' });

  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss, focus, hover, role]);

  return (
    <Utility vFlex vJustifyContent="center" vMargin={24}>
      <Button ref={refs.setReference} {...getReferenceProps()}>
        Primary action
      </Button>
      {isOpen && (
        <Tooltip
          ref={refs.setFloating}
          style={{
            left: x,
            position: strategy,
            top: y,
            width: 'fit-content',
          }}
          {...getFloatingProps()}
        >
          This is a tooltip
        </Tooltip>
      )}
    </Utility>
  );
};
```

### dropdown-menu

- **Description**: Interactive element enabling users to select a single option from a list.
- **Details**: [details](components/dropdown-menu.md)

**Example:**
```tsx
import { useClick, useFloating, useInteractions } from '@floating-ui/react';
import { VisaChevronDownTiny, VisaChevronUpTiny } from '@visa/nova-icons-react';
import { useState } from 'react';
import { Button, DropdownButton, DropdownMenu, Listbox, UtilityFragment } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'dropdown-menu-default';

export const DefaultDropdownMenu = () => {
  const [open, setOpen] = useState(false);

  const { context, floatingStyles, refs } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: 'bottom-start',
  });

  const onClick = useClick(context);

  const { getReferenceProps, getFloatingProps } = useInteractions([onClick]);

  return (
    // This div is not required, it's used to show the whole dropdown menu in the example
    <div style={{ blockSize: 250 }}>
      <DropdownButton
        aria-controls={id}
        aria-expanded={open}
        id={`${id}-button`}
        ref={refs.setReference}
        {...getReferenceProps()}
      >
        Action
        {open ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
      </DropdownButton>
      {open && (
        <DropdownMenu
          id={id}
          aria-hidden={!open}
          ref={refs.setFloating}
          style={{ inlineSize: '180px', ...floatingStyles }}
          {...getFloatingProps()}
        >
          <UtilityFragment vHide={!open}>
            <Listbox>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 1
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 3
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary" subtle>
                    Label 3
                  </Button>
                </UtilityFragment>
              </li>
              <li>
                <UtilityFragment
                  vFlex
                  vFlexRow
                  vAlignItems="start"
                  vGap={6}
                  vPaddingHorizontal={8}
                  vPaddingVertical={11}
                >
                  <Button className="v-listbox-item" colorScheme="tertiary">
                    Label 4
                  </Button>
                </UtilityFragment>
              </li>
            </Listbox>
          </UtilityFragment>
        </DropdownMenu>
      )}
    </div>
  );
};
```

### badge

- **Description**: Visual indicators communicating the status of a component.
- **Details**: [details](components/badge.md)

**Example:**
```tsx
import { VisaHistoryTiny } from '@visa/nova-icons-react';
import { Badge } from '@visa/nova-react';

export const SubtleBadgeDefault = () => {
  return (
      <Badge badgeType="subtle">
        <VisaHistoryTiny aria-label="history" /> Label
      </Badge>
  );
};
```

### chip

- **Description**: Compact elements used to filter content or display user input.
- **Details**: [details](components/chip.md)

**Example:**
```tsx
import { Checkbox, Chip } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-selection-chip';

export const DefaultSelectionChip = () => {
  return (
    <Chip chipType="selection" htmlFor={id} tag="label">
      Label
      <Checkbox id={id} />
    </Chip>
  );
};
```

### navigation-drawer

- **Description**: Collapsible panel or menu next to page content that links to important pages or features.
- **Details**: [details](components/navigation-drawer.md)

**Example:**
```tsx
import { VisaAccountTiny, VisaChevronDownTiny, VisaChevronUpTiny, VisaCloseTiny } from '@visa/nova-icons-react';
import {
  Button,
  Divider,
  Panel,
  Link,
  Nav,
  NavAppName,
  Tab,
  TabSuffix,
  Tabs,
  Typography,
  Utility,
  UtilityFragment,
  VisaLogo,
} from '@visa/nova-react';
import { CSSProperties, useState, useRef } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-navigation-drawer';
const navElAriaLabel = 'Default drawer';

const tabsContent = [
  {
    tabLabel: 'L1 label 1',
    id: `${id}-tab-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 2',
    id: `${id}-tab-1`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 3',
    id: `${id}-tab-2`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 4',
    id: `${id}-tab-3`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L1 label 5',
    id: `${id}-tab-4`,
    href: './navigation-drawer',
  },
];

const accountSubItems = [
  {
    tabLabel: 'L2 label 1',
    id: `${id}-account-sub-item-0`,
    href: './navigation-drawer',
  },
  {
    tabLabel: 'L2 label 2',
    id: `${id}-account-sub-item-1`,
    href: './navigation-drawer',
  },
];

export const DefaultNavigationDrawer = () => {
  const [accountTabOpen, setAccountTabOpen] = useState(false);
  const navDrawerRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <UtilityFragment vMargin={10}>
        <Button onClick={() => navDrawerRef.current?.showModal()}>Open drawer</Button>
      </UtilityFragment>

      <UtilityFragment vMarginHorizontal={0}>
        <Panel
          aria-modal="true"
          ref={navDrawerRef}
          id={id}
          tag="dialog"
          style={
            {
              '--v-panel-inline-size': 'initial',
            } as CSSProperties
          }
        >
          <Nav
            drawer
            orientation="vertical"
            tag="div"
            style={
              {
                inlineSize: '242px',
              } as CSSProperties
            }
          >
            <UtilityFragment vMarginRight={4} vMarginLeft="auto">
              <Button
                aria-label="Close"
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                onClick={() => navDrawerRef.current?.close()}
                subtle
              >
                <VisaCloseTiny />
              </Button>
            </UtilityFragment>
            <UtilityFragment
              vFlex
              vFlexCol
              vGap={12}
              vMarginTop={4}
              vMarginRight={16}
              vMarginBottom={16}
              vMarginLeft={24}
            >
              <Link
                aria-label="Visa Application Name Home"
                href="https://www.visa.com"
                id={`${id}-home-link`}
                noUnderline
                style={{ backgroundColor: 'transparent' }}
              >
                <VisaLogo />
                <NavAppName>
                  <Typography variant="subtitle-1">Application Name</Typography>
                </NavAppName>
              </Link>
            </UtilityFragment>
            <nav aria-label={navElAriaLabel}>
              <Tabs orientation="vertical">
                {tabsContent.map(tabContent => (
                  <Tab key={tabContent.id}>
                    <UtilityFragment vMarginLeft={14}>
                      <Button colorScheme="tertiary" element={<a href={tabContent.href}>{tabContent.tabLabel}</a>} />
                    </UtilityFragment>
                  </Tab>
                ))}
              </Tabs>
            </nav>
            <Utility vFlex vFlexCol vAlignSelf="stretch" vGap={4} vMarginTop="auto">
              <Divider dividerType="decorative" />
              <Tab tag="div">
                <Button
                  aria-expanded={accountTabOpen}
                  aria-controls={`${id}-account-sub-menu`}
                  aria-label="Alex Miller"
                  buttonSize="large"
                  colorScheme="tertiary"
                  onClick={() => setAccountTabOpen(!accountTabOpen)}
                >
                  <VisaAccountTiny />
                  Alex Miller
                  <TabSuffix element={accountTabOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />} />
                </Button>
                <UtilityFragment vHide={!accountTabOpen}>
                  <Tabs orientation="vertical" id={`${id}-account-sub-menu`} aria-hidden={!accountTabOpen}>
                    {accountSubItems.map(accountSubItem => (
                      <Tab key={accountSubItem.id} id={accountSubItem.id}>
                        <Button
                          colorScheme="tertiary"
                          element={<a href={accountSubItem.href}>{accountSubItem.tabLabel}</a>}
                        />
                      </Tab>
                    ))}
                  </Tabs>
                </UtilityFragment>
              </Tab>
            </Utility>
          </Nav>
        </Panel>
      </UtilityFragment>
    </>
  );
};
```

### multiselect

- **Description**: Control that allows users to select multiple options from a dropdown menu.
- **Details**: [details](components/multiselect.md)

**Example:**
```tsx
import { VisaChevronDownTiny, VisaChevronUpTiny, VisaClearAltTiny } from '@visa/nova-icons-react';
import {
  Button,
  Checkbox,
  Chip,
  Combobox,
  DropdownContainer,
  Input,
  InputContainer,
  Label,
  Listbox,
  ListboxContainer,
  ListboxItem,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { UseComboboxState, UseComboboxStateChangeOptions, useCombobox, useMultipleSelection } from 'downshift';
import { useState } from 'react';

type Item = { value: string };

const id = 'default-multiselect';
const multiselectItems: Item[] = [
  { value: 'Option A' },
  { value: 'Option B' },
  { value: 'Option C' },
  { value: 'Option D' },
  { value: 'Option E' },
];

export const itemToString = (item: Item | null) => (item ? item.value : '');

export const comboboxStateReducer = <ItemType,>(
  state: UseComboboxState<ItemType>,
  { type, changes }: UseComboboxStateChangeOptions<ItemType>
) => {
  switch (type) {
    case useCombobox.stateChangeTypes.InputClick:
      return {
        // don't open the menu just because the input was clicked
        // instead, wait for an keystroke or a toggle button click
        ...state,
      };
    case useCombobox.stateChangeTypes.InputChange:
      return {
        ...changes,
        // don't update the highlighted index
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.ItemMouseMove:
    case useCombobox.stateChangeTypes.MenuMouseLeave:
      return {
        ...changes,
        // don't change the focused item just because the mouse moved
        highlightedIndex: state.highlightedIndex,
      };
    case useCombobox.stateChangeTypes.InputKeyDownEnter:
    case useCombobox.stateChangeTypes.ItemClick:
      return {
        ...changes,
        isOpen: true, // keep the menu open on item select or Enter press
        // and if we're selecting an item, maintain the same highlightedIndex
        ...(changes.selectedItem && { highlightedIndex: state.highlightedIndex }),
      };
    default:
      return changes;
  }
};

export const DefaultMultiselect = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedItems, setSelectedItems] = useState<Item[]>([]);
  const items = multiselectItems;

  const { getDropdownProps, removeSelectedItem } = useMultipleSelection({
    selectedItems,
    onStateChange({ selectedItems: newSelectedItems, type }) {
      if (
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.SelectedItemKeyDownDelete ||
        type === useMultipleSelection.stateChangeTypes.DropdownKeyDownBackspace ||
        type === useMultipleSelection.stateChangeTypes.FunctionRemoveSelectedItem
      ) {
        setSelectedItems(newSelectedItems!);
      }
    },
  });
  const {
    getToggleButtonProps,
    getLabelProps,
    getMenuProps,
    getInputProps,
    getItemProps,
    highlightedIndex,
    isOpen,
    setHighlightedIndex,
  } = useCombobox({
    items,
    itemToString,
    inputValue,
    stateReducer: comboboxStateReducer,
    onStateChange({ inputValue: newInputValue, type, selectedItem }) {
      if (type === useCombobox.stateChangeTypes.InputChange) {
        setInputValue(newInputValue!);
      }
      if (type === useCombobox.stateChangeTypes.ItemClick && !!selectedItem) {
        // make sure the highlighted index is on the item that was just clicked
        setHighlightedIndex(items.indexOf(selectedItem));
      }
    },
  });

  return (
    <Combobox>
      <UtilityFragment vFlex vFlexCol vGap={4}>
        <DropdownContainer>
          <Label {...getLabelProps()}>Label (required)</Label>
          <UtilityFragment vPaddingVertical={3} vPaddingLeft={3} vPaddingRight={6}>
            <InputContainer>
              <Utility vFlex vFlexGrow vFlexShrink vFlexWrap vGap={2}>
                {selectedItems.map((item, index) => (
                  <UtilityFragment vFlexShrink0 key={`selected-item-${index}`}>
                    <Chip chipSize="compact">
                      <Label>{item.value}</Label>
                      <Button
                        aria-label={`Remove ${item.value}`}
                        colorScheme="tertiary"
                        iconButton
                        onClick={() => removeSelectedItem(item)}
                        subtle
                      >
                        <VisaClearAltTiny />
                      </Button>
                    </Chip>
                  </UtilityFragment>
                ))}
                <UtilityFragment vFlexShrink style={{ flexBasis: '50px' }}>
                  <Input
                    name={id}
                    {...getInputProps(
                      getDropdownProps({
                        onKeyDown: e => {
                          if (e.key === 'Enter') {
                            if (highlightedIndex !== -1 && isOpen) {
                              const selectedItem = items[highlightedIndex];
                              if (selectedItems.includes(selectedItem)) {
                                removeSelectedItem(selectedItem);
                              } else {
                                setSelectedItems([...selectedItems, selectedItem]);
                                setInputValue('');
                              }
                            }
                          }
                        },
                      })
                    )}
                  />
                </UtilityFragment>
              </Utility>
              <Button
                aria-haspopup="listbox"
                aria-label={`${id}-toggle-button`}
                buttonSize="small"
                colorScheme="tertiary"
                iconButton
                {...getToggleButtonProps()}
              >
                {isOpen ? <VisaChevronUpTiny /> : <VisaChevronDownTiny />}
              </Button>
            </InputContainer>
          </UtilityFragment>
        </DropdownContainer>
      </UtilityFragment>
      <ListboxContainer>
        <UtilityFragment vFlex>
          <Listbox {...getMenuProps()}>
            {items.map((item, index) => (
              <ListboxItem<HTMLLIElement>
                key={`${id}-example-${index}`}
                className={highlightedIndex === index ? 'v-listbox-item-highlighted' : ''}
                {...getItemProps({
                  item,
                  index,
                  'aria-selected': selectedItems.includes(item),
                  onClick: () => {
                    if (selectedItems.includes(item)) {
                      removeSelectedItem(item);
                    } else {
                      setSelectedItems([...selectedItems, item]);
                      setInputValue('');
                    }
                  },
                })}
              >
                <Checkbox tag="span" />
                {item.value}
              </ListboxItem>
            ))}
          </Listbox>
        </UtilityFragment>
      </ListboxContainer>
    </Combobox>
  );
};
```

### divider

- **Description**: Visual element used to separate and group information on a page.
- **Details**: [details](components/divider.md)

**Example:**
```tsx
import { Divider } from '@visa/nova-react';

export const DefaultDivider = () => {
  return <Divider />;
};
```

### anchor-link-menu

- **Description**: Menu of links that navigate to sections within the current page.
- **Details**: [details](components/anchor-link-menu.md)

**Example:**
```tsx
import { AnchorLinkMenu, AnchorLinkMenuHeader, Link, Typography } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-anchor-link-menu';

export const DefaultAnchorLinkMenu = () => {
  return (
    <AnchorLinkMenu aria-labelledby={`${id}-header`}>
      <section>
        <AnchorLinkMenuHeader>
          <Typography id={`${id}-header`} tag="h2" variant="overline">
            Section title
          </Typography>
        </AnchorLinkMenuHeader>
        <ul>
          <li>
            <Link aria-current="true" href="./anchor-link-menu">
              L1 label 1
            </Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 2</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 3</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 4</Link>
          </li>
          <li>
            <Link href="./anchor-link-menu">L1 label 5</Link>
          </li>
        </ul>
      </section>
    </AnchorLinkMenu>
  );
};
```

## Hooks

### use-card-number-validation

- **Description**: This hook is used to to validate card numbers. This hook uses BIN regex's, length, Luhn checksum algorithm (modulo 10 check), and brands to check card number validity. This hook is designed to be flexible and allow for custom validators.
- **Details**: [details](components/use-card-number-validation.md)

**Example:**
```tsx
import { VisaChevronDownTiny } from '@visa/nova-icons-react';
import {
  Divider,
  Input,
  InputContainer,
  InputControl,
  Label,
  Select,
  Switch,
  SwitchLabel,
  useCardNumberValidation,
  Typography,
  Utility,
} from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'use-card-validation-example';

export const UseCardValidationUsage = () => {
  /// These states are for demo purposes:
  const [cardNumberInputValueKey, setCardNumberInputValueKey] = useState('cardNumberInputValue');
  const [trimToMaxLength, setTrimToMaxLength] = useState(true);

  const {
    binValid,
    brand,
    brandValid,
    cardNumberInputValue,
    cardNumberValidator,
    cleanCardNumber,
    formattedCardNumber,
    lastDigitValid,
    lengthValid,
    onCardNumberChange,
    valid,
  } = useCardNumberValidation({
    allowedBrands: ['VISA'],
    defaultCardNumberInputValue: '40000000 hello world 00000000 000000',
    trimToMaxLength,
  });

  const valueMap: Record<string, string> = { cardNumberInputValue, cleanCardNumber, formattedCardNumber };
  const valueMapKeys = Object.keys(valueMap);

  return (
    <Utility vFlexCol vGap={16}>
      <Utility vFlex vFlexCol vGap={4}>
        <Label htmlFor={`${id}-card-number-input`}>Visa card number</Label>
        <InputContainer>
          <Input
            aria-required="true"
            autoComplete="cc-number"
            id={`${id}-card-number-input`}
            onChange={event => onCardNumberChange(event.currentTarget.value)}
            required
            type="text"
            value={valueMap[cardNumberInputValueKey]}
          />
        </InputContainer>
      </Utility>
      <code>binValid: {binValid.toString()}</code>
      <code>brand: {brand ?? 'undefined'}</code>
      <code>brandValid: {brandValid.toString()}</code>
      <code>cardNumberInputValue: {cardNumberInputValue}</code>
      <code>cardNumberValidator.brand: {cardNumberValidator?.brand ?? 'undefined'}</code>
      <code>cardNumberValidator.maxLength: {cardNumberValidator?.maxLength ?? 'undefined'}</code>
      <code>cleanCardNumber: {cleanCardNumber}</code>
      <code>formattedCardNumber: {formattedCardNumber}</code>
      <code>lastDigitValid: {lastDigitValid.toString()}</code>
      <code>lengthValid: {lengthValid.toString()}</code>
      <code>valid: {valid.toString()}</code>

      <Divider />

      <Typography tag="span" variant="body-2-bold">
        Demo options:
      </Typography>
      <Utility tag="fieldset" vFlex vFlexCol vGap={6}>
        <Label htmlFor={`${id}-input-value-key-select`}>Visa card number input value</Label>
        <InputContainer>
          <Select
            id={`${id}-input-value-key-select`}
            name="select-default-example"
            onChange={event => setCardNumberInputValueKey(event.currentTarget.value)}
            value={cardNumberInputValueKey}
          >
            {valueMapKeys.map(key => (
              <option key={key} value={key}>
                {key}
              </option>
            ))}
          </Select>
          <InputControl>
            <VisaChevronDownTiny />
          </InputControl>
        </InputContainer>
      </Utility>
      <Utility vFlex vFlexWrap vGap={10} vJustifyContent="between" vMargin={8}>
        <SwitchLabel htmlFor={`${id}-trim-value-switch`}>
          <code>trimToMaxLength</code>
        </SwitchLabel>
        <Switch
          checked={trimToMaxLength}
          id={`${id}-trim-value-switch`}
          name={`${id}-trim-value-switch`}
          onChange={event => setTrimToMaxLength(event.currentTarget.checked)}
        />
      </Utility>
    </Utility>
  );
};
```

### use-tabs

- **Description**: This hook allows us to set the <defaultSelected> value, which indicates that we are selecting that item by default.
- **Details**: [details](components/use-tabs.md)

**Example:**
```tsx
import { Button, Tab, Tabs, useTabs } from '@visa/nova-react';

const tabsList = ['Tab 1', 'Tab 2', 'Tab 3'];

export const UseTabsExample = () => {
  const { getTabIndex, onIndexChange, onKeyNavigation, ref: tabsRef, selectedIndex } = useTabs();

  return (
    <Tabs onKeyDown={onKeyNavigation} role="tablist">
      {tabsList.map((tab, index) => (
        <Tab key={`use-tabs-horizontal-tab-${index}`} role="none">
          <Button
            aria-selected={index === selectedIndex}
            buttonSize="large"
            colorScheme="tertiary"
            onClick={() => onIndexChange(index)}
            ref={el => {
              tabsRef.current[index] = el;
            }}
            role="tab"
            tabIndex={getTabIndex(index)}
          >
            {tab}
          </Button>
        </Tab>
      ))}
    </Tabs>
  );
};
```

### use-debounce

- **Description**: Debounces expensive function, only calling the function after it's last call has waited for specified delay
- **Details**: [details](components/use-debounce.md)

**Example:**
```tsx
import { Button, Typography, Utility, useDebounce } from '@visa/nova-react';
import { VisaInformationTiny, VisaSuccessTiny } from "@visa/nova-icons-react";
import { useState, CSSProperties } from 'react';

export const UseButtonDebounceExample = () => {
  const [success, setSuccess] = useState(false);

  const onDebouncedClick = useDebounce(() => {
    setSuccess(true);
  }, 1000);

  return (
    <Utility vFlex vFlexCol vGap={12}>
      <Typography tag="span" variant="body-2-bold">
        Rapidly click the button in sequence, then wait for one second:
      </Typography>

      <Utility vFlex vFlexRow vGap={12}>
        <Button onClick={onDebouncedClick}>Submit debounced</Button>
        <Button colorScheme="secondary" onClick={() => setSuccess(false)}>
          Reset
        </Button>
      </Utility>

      <Typography aria-atomic="true" aria-live="assertive" style={{lineHeight: '16px'}}>
        {success ? <VisaSuccessTiny style={{ '--v-icon-primary': 'green', '--v-icon-secondary': 'var(--v-message-text-success)', marginInlineEnd: '3px', verticalAlign: 'bottom' } as CSSProperties} /> : 
        <VisaInformationTiny style={{ '--v-icon-primary': 'var(--palette-default-text-subtle)', '--v-icon-secondary': 'var(--palette-default-text-subtle)', marginInlineEnd: '3px', verticalAlign: 'bottom' } as CSSProperties} />}
        {success ? 'Button click successful, many thanks' : 'Waiting for button click'}
      </Typography>
    </Utility>
  );
};
```

### use-accordion

- **Description**: This hook is used to manage the open state and keyboard navigation of accordions.
- **Details**: [details](components/use-accordion.md)

**Example:**
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  useAccordion,
} from '@visa/nova-react';
import { Fragment } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'use-accordion-usage';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Section label 1',
  },
];

export const UseAccordionExample = () => {
  // useAccordion hook returns the following:
  // isIndexExpanded: function that returns a boolean value to determine if the accordion is expanded or not
  // onKeyNavigation: function that handles keyboard navigation, and toggles the accordion expanded state
  // ref: a ref object that is used to store the accordion elements
  // toggleIndexExpanded: function that toggles the accordion expanded state, based on the index provided
  const { isIndexExpanded, onKeyNavigation, ref, toggleIndexExpanded } = useAccordion();

  return (
    <Accordion id={id} onKeyDown={onKeyNavigation} tag="div">
      {accordions.map((accordion, i) => (
        <Fragment key={i}>
          <AccordionHeading
            aria-controls={`${id}-panel-${i}`}
            aria-expanded={isIndexExpanded(i)}
            buttonSize="large"
            colorScheme="secondary"
            id={`${id}-header-${i}`}
            onClick={() => toggleIndexExpanded(i)}
            ref={el => {
              ref.current[i] = el;
            }}
            tag="button"
          >
            <AccordionToggleIcon accordionOpen={isIndexExpanded(i)} />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel aria-hidden={!isIndexExpanded(i)} id={`${id}-panel-${i}`}>
            <Typography tag="span">{accordion.content}</Typography>
          </AccordionPanel>
        </Fragment>
      ))}
    </Accordion>
  );
};
```

### use-pagination

- **Description**: This hook is used to manage pagination events, state, and visible page blocks.
- **Details**: [details](components/use-pagination.md)

**Example:**
```tsx
import {
  VisaArrowEndTiny,
  VisaArrowStartTiny,
  VisaChevronLeftTiny,
  VisaChevronRightTiny,
  VisaOptionHorizontalTiny,
} from '@visa/nova-icons-react';
import { Button, Pagination, PaginationOverflow, UtilityFragment, usePagination } from '@visa/nova-react';

export const UsePaginationExample = () => {
  const {
    isFirstPage,
    isLastPage,
    onFirstPage,
    onLastPage,
    onNextPage,
    onPageChange,
    onPreviousPage,
    pages,
    selectedPage,
  } = usePagination({ maxPageNumber: 10, startPage: 1, totalPages: 12 });

  return (
    <nav aria-label="minimum and maximum pagination" role="navigation">
      <UtilityFragment vAlignItems="center" vFlex vFlexRow vGap={4}>
        <Pagination>
          <li>
            <Button
              aria-label="Go to first page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isFirstPage}
              iconButton
              onClick={onFirstPage}
            >
              <VisaArrowStartTiny rtl />
            </Button>
          </li>
          <li>
            <Button
              aria-label="Go to previous page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isFirstPage}
              iconButton
              onClick={onPreviousPage}
            >
              <VisaChevronLeftTiny rtl />
            </Button>
          </li>
          {pages.map((pageNumber, index) =>
            pageNumber === -1 ? (
              <UtilityFragment key={`min-max-pagination-ellipse-${index}`} vAlignItems="center" vFlex>
                <PaginationOverflow>
                  <VisaOptionHorizontalTiny />
                </PaginationOverflow>
              </UtilityFragment>
            ) : (
              <li key={`min-max-pagination-page-${pageNumber}`}>
                <Button
                  aria-current={selectedPage === pageNumber}
                  aria-label={`Page ${pageNumber}`}
                  colorScheme="tertiary"
                  onClick={() => onPageChange(pageNumber as number)}
                >
                  {pageNumber}
                </Button>
              </li>
            )
          )}
          <li>
            <Button
              aria-label="Go to next page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isLastPage}
              iconButton
              onClick={onNextPage}
            >
              <VisaChevronRightTiny rtl />
            </Button>
          </li>
          <li>
            <Button
              aria-label="Go to last page"
              buttonSize="small"
              colorScheme="tertiary"
              disabled={isLastPage}
              iconButton
              onClick={onLastPage}
            >
              <VisaArrowEndTiny rtl />
            </Button>
          </li>
        </Pagination>
      </UtilityFragment>
    </nav>
  );
};
```

### use-listbox

- **Description**: This hook is used to manage the selected state and keyboard navigation of listbox component.
- **Details**: [details](components/use-listbox.md)

**Example:**
```tsx
import { Label, Listbox, ListboxContainer, ListboxItem, useListbox } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'use-listbox-usage';

const options = [
  {
    label: 'Item A',
  },
  {
    disabled: true,
    label: 'Item B',
  },
  {
    label: 'Item C',
  },
  {
    label: 'Item D',
  },
  {
    label: 'Item E',
  },
];

export const UseListboxExample = () => {
  // useListbox hook returns the following:
  // isIndexSelected: function that returns a boolean value to determine if the index is selected or not
  // getTabIndex: function that returns the correct tabIndex based on the index and disabled state
  // onKeyNavigation: function that handles keyboard navigation, and toggles the list item selected state
  // ref: a ref object that is used to store the list item elements
  // toggleIndexSelected: function that toggles the list item selected state, based on the index provided
  const { isIndexSelected, getTabIndex, onKeyNavigation, ref, toggleIndexSelected } = useListbox({
    defaultSelected: 0,
  }); // Default to active on first list item

  return (
    <fieldset>
      <Label id={`${id}-legend`} tag="legend">
        Label (required)
      </Label>
      <ListboxContainer>
        <Listbox aria-labelledby={`${id}-legend`} id={id} onKeyDown={onKeyNavigation} role="listbox" scroll>
          {options.map((option, index) => (
            <ListboxItem
              aria-disabled={option.disabled}
              aria-selected={isIndexSelected(index)}
              key={`${id}-option-${index}`}
              onClick={() => toggleIndexSelected(index)}
              ref={el => {
                ref.current[index] = el;
              }}
              role="option"
              tabIndex={getTabIndex(index, option.disabled)}
            >
              <span className="v-radio v-flex-shrink-0 " />
              {option.label}
            </ListboxItem>
          ))}
        </Listbox>
      </ListboxContainer>
    </fieldset>
  );
};
```

### use-focus-trap

- **Description**: This hook is used to trap focus inside a container.
- **Details**: [details](components/use-focus-trap.md)

**Example:**
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
const id = 'use-focus-trap-usage';

export const UseFocusTrapExample = () => {
  const { onKeyNavigation, ref } = useFocusTrap();

  return (
    <>
      <Button onClick={() => ref.current?.showModal()}>Open dialog</Button>
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
          <Utility vAlignItems="center" vFlex vFlexWrap vGap={8} vJustifyContent="end" vPaddingTop={16}>
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

### use-wizard

- **Description**: This hook is used to control the state of a wizard component.
- **Details**: [details](components/use-wizard.md)

**Example:**
```tsx
import { Badge, Button, Utility, Wizard, WizardStep, useWizard } from '@visa/nova-react';
import { VisaCheckmarkTiny, VisaChevronRightTiny, VisaErrorAltTiny } from '@visa/nova-icons-react';

const stepList = [
  { title: 'Step label 1' },
  { title: 'Step label 2' },
  { title: 'Step label 3' },
  { title: 'Step label 4' },
  { title: 'Step label 5' },
];

export const UseWizardExample = () => {
  const {
    currentStep,
    isLastStep,
    isStepAvailable,
    isStepComplete,
    isStepError,
    onStepChange,
    onStepComplete,
    onStepError,
    onStepNext,
    onStepPrevious,
    onStepReset,
    onWizardReset,
  } = useWizard({ length: stepList.length });

  return (
    <Utility vFlex vFlexCol vGap={12}>
      <Wizard>
        {stepList.map((step, i) => (
          <WizardStep key={`horizontal-wizard-step-${i + 1}`}>
            {isStepAvailable(i) ? (
              <Button
                className={`${
                  currentStep === i ? 'v-typography-label-large-active' : 'v-typography-body-2'
                } v-typography-color-default v-gap-8`}
                colorScheme="tertiary"
                onClick={() => {
                  onStepChange(i);
                }}
              >
                <Badge
                  active={currentStep === i && !isStepError(i) && !isStepComplete(i)}
                  badgeType={(isStepError(i) && 'critical') || (isStepComplete(i) && 'stable') || 'subtle'}
                  badgeVariant="icon"
                  clear={!(currentStep === i)}
                  tag="span"
                >
                  {isStepError(i) ? <VisaErrorAltTiny /> : isStepComplete(i) ? <VisaCheckmarkTiny /> : i + 1}
                </Badge>
                {step.title}
                {i < stepList.length - 1 && <VisaChevronRightTiny className="v-typography-color-subtle" />}
              </Button>
            ) : (
              <>
                <Badge badgeType="subtle" badgeVariant="icon" clear tag="span">
                  {i + 1}
                </Badge>
                {step.title}
                {!isLastStep(i) && <VisaChevronRightTiny className="v-typography-color-subtle" />}
              </>
            )}
          </WizardStep>
        ))}
      </Wizard>
      <Utility vFlex vFlexWrap vGap={24} vJustifyContent="between">
        <Button onClick={onStepPrevious}>Previous step</Button>
        <Utility vFlex vFlexWrap vGap={12}>
          <Button colorScheme="secondary" onClick={() => onStepComplete(currentStep, { autoProgress: false })}>
            Set step successful
          </Button>
          <Button colorScheme="secondary" onClick={() => onStepError(currentStep, { autoProgress: false })}>
            Set step error
          </Button>
          <Button colorScheme="secondary" onClick={() => onStepReset(currentStep)}>
            Reset current step
          </Button>
        </Utility>
        <Button onClick={onStepNext}>Next step</Button>
      </Utility>
      <Utility vFlex vFlexWrap vGap={16} vJustifyContent="center">
        <Button destructive onClick={() => onWizardReset()}>
          Reset wizard
        </Button>
        <Button colorScheme="secondary" destructive onClick={() => onWizardReset(1)}>
          Reset to step 2
        </Button>
      </Utility>
    </Utility>
  );
};
```

## Utilities

### breakpoints

- **Description**: 
- **Details**: [details](components/breakpoints.md)

**Example:**
```tsx
import { Avatar, Button, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const HideBreakpoints = () => {
  const [hide, setHide] = useState(false);
  const [toggled, setToggled] = useState(false);

  const toggleHide = (changedHide: boolean) => {
    setHide(changedHide);
    setToggled(true);
  };

  return (
    <Utility vFlex vGap={24} vAlignItems="center">
      <Utility element={<Avatar>AM</Avatar>} vHide={hide} />
      <span role="alert" aria-live="polite" className='v-sr'>
          {toggled && (
            hide? 'The avatar is hidden' : 'The avatar is visible'
          )}
        </span>
      <Button colorScheme="secondary" onClick={() => toggleHide(!hide)}>
        {hide ? 'Show' : 'Hide'}
      </Button>
    </Utility>
  );
};
```

### accessibility

- **Description**: Text elements to only be read by screen readers but not shown visually on screen.
- **Details**: [details](components/accessibility.md)

**Example:**
```tsx
import { ScreenReader } from '@visa/nova-react';

export const ScreenReaderOnlyText = () => {
  return <ScreenReader>This text is not shown on the screen, but it's accessible to a screen reader.</ScreenReader>;
};
```

### flex

- **Description**: 
- **Details**: [details](components/flex.md)

**Example:**
```tsx
import { Utility } from '@visa/nova-react';

export const DefaultFlex = () => {
  return (
    <Utility vFlex vGap={4}>
      This is a flex container
    </Utility>
  );
};
```

### spacing

- **Description**: 
- **Details**: [details](components/spacing.md)

**Example:**
```tsx
import { Surface, Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

export const GapSpacing = () => {
  const itemCardStyles = { boxShadow: 'var(--elevation-medium)', inlineSize: 'auto' } as CSSProperties;
  return (
    <Utility vFlex>
      <Utility vFlex vColGap={20} style={{ background: 'var(--palette-default-surface-highlight)' } as CSSProperties}>
        <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
          Item 1
        </Utility>
        <Utility vFlexGrow vPadding={16} style={itemCardStyles} element={<Surface />}>
          Item 2
        </Utility>
      </Utility>
    </Utility>
  );
};
```

### elevation

- **Description**: 
- **Details**: [details](components/elevation.md)

**Example:**
```tsx
import { Utility } from '@visa/nova-react';
import { CSSProperties } from 'react';

// These styles simply makes a square box for demo purposes.
const defaultBoxStyle: CSSProperties = {
  alignItems: 'center',
  background: 'var(--palette-default-surface-2, #FFF)',
  display: 'flex',
  blockSize: 100,
  inlineSize: 100,
  justifyContent: 'center',
};

export const AllElevation = () => {
  return (
    <Utility vFlex vFlexWrap vGap={12}>
      <Utility vElevation="none" style={defaultBoxStyle}>
        None
      </Utility>
      <Utility vElevation="inset" style={defaultBoxStyle}>
        Inset
      </Utility>
      <Utility vElevation="xsmall" style={defaultBoxStyle}>
        XSmall
      </Utility>
      <Utility vElevation="small" style={defaultBoxStyle}>
        Small
      </Utility>
      <Utility vElevation="medium" style={defaultBoxStyle}>
        Medium
      </Utility>
      <Utility vElevation="large" style={defaultBoxStyle}>
        Large
      </Utility>
      <Utility vElevation="xlarge" style={defaultBoxStyle}>
        XLarge
      </Utility>
      <Utility vElevation="xxlarge" style={defaultBoxStyle}>
        XXLarge
      </Utility>
    </Utility>
  );
};
```

