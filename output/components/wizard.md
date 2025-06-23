# wizard

## Metadata
- **Version**: 0.0.1
- **Description**: Manages and navigates multi-step processes within your application.
- **Category**: components

## Example Sections
1. **Multi-page wizards**
   - Description: 
2. **Single-page wizard**
   - Description: 
3. **Custom wizard**
   - Description: 

## Examples
### Horizontal multi-page wizard
- **Section**: Multi-page wizards
- **URL**: components/wizard/horizontal-wizard
- **Tags**: 
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

### Vertical multi-page wizard
- **Section**: Multi-page wizards
- **URL**: components/wizard/vertical-wizard
- **Tags**: 
```tsx
import {
  VisaArrowBackTiny,
  VisaArrowForwardTiny,
  VisaCheckmarkTiny,
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
const id = 'vertical-multi-page-wizard';
const navRegionAriaLabel = 'Vertical multi-page wizard';

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

export const VerticalWizard = () => {
  const {
    currentStep,
    isStepAvailable,
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
    <Utility vFlex vFlexCol vJustifyContent="end" vFlexGrow vGap={10}>
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
          <Utility vFlexGrow vJustifyContent="end" vFlex vFlexWrap vColGap={24} vRowGap={16}>
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
    <Utility vFlex vFlexWrap vGap={12}>
      <nav aria-label={navRegionAriaLabel}>
        <Wizard vertical>
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
                      active={currentStep === i && !isStepError(i) && !isStepComplete(i)}
                      badgeType={isStepError(i) ? 'critical' : isStepComplete(i) ? 'stable' : 'subtle'}
                      badgeVariant="icon"
                      clear={i !== currentStep}
                      tag="span"
                    >
                      {isStepError(i) ? <VisaErrorAltTiny /> : isStepComplete(i) ? <VisaCheckmarkTiny /> : step.label}
                    </Badge>
                    <Typography>{step.title}</Typography>
                  </Button>
                </>
              ) : (
                <>
                  <ScreenReader>
                    {`${isStepError(i) ? 'Error ' : isStepComplete(i) ? 'Completed ' : ''}Step ${i + 1} of ${steps.length}`}
                  </ScreenReader>
                  <Badge
                    active={currentStep === i && !isStepError(i) && !isStepComplete(i)}
                    clear={i !== currentStep}
                    badgeType={isStepError(i) ? 'critical' : isStepComplete(i) ? 'stable' : 'subtle'}
                    badgeVariant="icon"
                    tag="span"
                  >
                    {isStepError(i) ? <VisaErrorAltTiny /> : isStepComplete(i) ? <VisaCheckmarkTiny /> : step.label}
                  </Badge>
                  <Typography variant={i === currentStep ? 'label-large-active' : 'body-2'}>{step.title}</Typography>
                </>
              )}
            </WizardStep>
          ))}
        </Wizard>
      </nav>
      <Utility vFlex vFlexCol vFlexGrow vGap={12}>
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
        <Utility vFlex vFlexCol vGap={12} vJustifyContent="between" vFlexGrow>
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
              </Utility>
            );
          })}
          {currentStep === steps.length - 1 && renderSummaryStep()}
          {renderActionButtons()}
        </Utility>
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

### Default single-page wizard
- **Section**: Single-page wizard
- **URL**: components/wizard/single-page-wizard
- **Tags**: 
```tsx
import {
  VisaArrowBackTiny,
  VisaArrowForwardTiny,
  VisaCheckmarkTiny,
  VisaEditTiny,
  VisaErrorAltTiny,
  VisaErrorTiny,
  VisaSuccessHigh,
} from '@visa/nova-icons-react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Badge,
  Button,
  Dialog,
  DialogCloseButton,
  DialogContent,
  DialogHeader,
  DialogIcon,
  Divider,
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
import { CSSProperties, ChangeEvent, useEffect, useRef, useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'single-page-wizard';
const navRegionAriaLabel = 'Single page wizard';

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

export const SinglePageWizard = () => {
  const {
    currentStep,
    isStepAvailable,
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

  const handleClickNext = () => {
    if (!inputValues[currentStep]) {
      onStepError(currentStep);
      // find the input element with the error in the refs map and set focus on it
      const inputRefsMap = getInputRefMap();
      const errorStepInputNode = inputRefsMap.get(steps[currentStep].inputId);
      errorStepInputNode.focus();
      return;
    }

    setHasWizardStepChanged(true);
    setShowSavedFlag(false);
    onStepComplete(currentStep);
  };

  const handleClickPrevious = () => {
    setShowSavedFlag(false);
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

  const handleClickStep = (i: number) => {
    setHasWizardStepChanged(true);
    onStepChange(i);
  };

  const renderActionButtons = () => {
    return (
      <Utility vPaddingVertical={12} vPaddingHorizontal={40}>
        <Utility vFlex vFlexWrap vJustifyContent="between" vColGap={24} vRowGap={16}>
          <Utility vJustifyContent="start" vFlex vFlexWrap vColGap={24} vRowGap={16}>
            <Button onClick={handleSave} colorScheme="secondary">
              Save
            </Button>
            <Button onClick={handleExit} colorScheme="tertiary">
              Exit
            </Button>
          </Utility>
          <Utility vFlexGrow vJustifyContent="end" vFlex vFlexWrap vColGap={24} vRowGap={16}>
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

  const renderSummaryStep = () => (
    <UtilityFragment vPaddingHorizontal={40}>
      <Surface>
        <Utility vFlexGrow>
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
  );

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
    <nav aria-label={navRegionAriaLabel}>
      <UtilityFragment vFlex vFlexCol vGap={16}>
        <Wizard tag="div">
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
          {steps.map((step, i) => (
            <WizardStep
              element={<Accordion tag="div" />}
              key={`${id}-step-${i + 1}`}
              aria-current={currentStep === i ? 'step' : undefined}
            >
              <UtilityFragment vFlex vJustifyContent="between">
                <AccordionHeading
                  aria-controls={`${id}-panel-${i}`}
                  aria-expanded={i === currentStep}
                  buttonSize="large"
                  colorScheme="secondary"
                  disabled={!isStepAvailable(i)}
                  id={`${id}-${i}`}
                  onClick={() => handleClickStep(i)}
                  ref={node => {
                    const map = getButtonRefMap();
                    if (node) {
                      // store the node in the inputRefs Map
                      map.set(step.buttonId, node);
                    } else {
                      map.delete(step.buttonId);
                    }
                  }}
                  tag="button"
                >
                  <Utility vAlignItems="center" vFlex vGap={6}>
                    <Badge
                      aria-current={i === currentStep ? 'step' : undefined}
                      aria-label={`${isStepError(i) ? 'Error ' : isStepComplete(i) ? 'Completed ' : ''}Step ${i + 1} of ${steps.length}`}
                      active={i === currentStep && !isStepError(i) && !isStepComplete(i)}
                      badgeType={isStepError(i) ? 'critical' : isStepComplete(i) ? 'stable' : 'subtle'}
                      clear={i !== currentStep}
                      badgeVariant="icon"
                      tag="span"
                      style={{ '--v-badge-disabled-background': 'var(--v-badge-subtle-icon-color)' } as CSSProperties}
                    >
                      {isStepError(i) ? (
                        <VisaErrorAltTiny aria-hidden="false" aria-label="error icon" />
                      ) : isStepComplete(i) ? (
                        <VisaCheckmarkTiny aria-hidden="false" aria-label="check mark icon" />
                      ) : (
                        step.label
                      )}
                    </Badge>
                    <Typography colorScheme={i === currentStep ? 'active' : isStepAvailable(i) ? 'default' : 'subtle'}>
                      {step.title}
                    </Typography>
                  </Utility>
                  <AccordionToggleIcon accordionOpen={i === currentStep} />
                </AccordionHeading>
              </UtilityFragment>
              <UtilityFragment vPaddingVertical={0} vPaddingHorizontal={0}>
                <AccordionPanel aria-hidden={i !== currentStep} id={`${id}-panel-${i}`}>
                  {i !== steps.length - 1 ? (
                    <Utility vPaddingVertical={12} vFlex vFlexCol vJustifyContent="between">
                      <Utility vPaddingVertical={12} vPaddingHorizontal={40} vFlex vFlexCol vGap={4}>
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
                                map.set(step.inputId, node);
                              } else {
                                map.delete(step.inputId);
                              }
                            }}
                          />
                        </InputContainer>
                        {isStepError(i) && (
                          <InputMessage
                            aria-atomic="true"
                            aria-live="assertive"
                            id={`${step.inputId}-message`}
                            role="alert"
                          >
                            <VisaErrorTiny />
                            This is required text that describes the error in more detail.
                          </InputMessage>
                        )}
                      </Utility>
                      <UtilityFragment vMarginVertical={12}>
                        <Divider dividerType="decorative" />
                      </UtilityFragment>
                      {renderActionButtons()}
                    </Utility>
                  ) : (
                    <Utility vPaddingVertical={12} vFlex vFlexCol vJustifyContent="between">
                      {renderSummaryStep()}
                      <UtilityFragment vMarginVertical={12}>
                        <Divider dividerType="decorative" />
                      </UtilityFragment>
                      {renderActionButtons()}
                    </Utility>
                  )}
                </AccordionPanel>
              </UtilityFragment>
            </WizardStep>
          ))}
        </Wizard>
      </UtilityFragment>
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
    </nav>
  );
};

```

### Responsive horizontal wizard
- **Section**: Custom wizard
- **URL**: components/wizard/responsive-horizontal-wizard
- **Tags**: 
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
  useWizard,
} from '@visa/nova-react';
import { CSSProperties, useEffect, useState, useRef, ChangeEvent } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'responsive-horizontal-wizard';
const navRegionAriaLabel = 'Responsive horizontal wizard';

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

const DEFAULT_INPUT_VALUES = Array(steps.length).fill('');

export const ResponsiveHorizontalWizard = () => {
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
    const buttonRefsMap = getButtonRefMap();
    const currentStepButtonNode = buttonRefsMap.get(steps[currentStep].buttonId);
    // the wizard steps are only buttons on the full size wizard.
    // if the button is available and NOT hidden then the full size
    // wizard is being rendered. focus the current step button.
    if (
      currentStepButtonNode &&
      currentStepButtonNode.offsetParent !== null &&
      window.getComputedStyle(currentStepButtonNode).display !== 'none'
    ) {
      currentStepButtonNode.focus();
      return;
    }
    // for the compact wizard, the steps are not buttons.
    // look for an inputRef on the current step to focus instead
    const inputRefsMap = getInputRefMap();
    const currentStepInputNode = inputRefsMap.get(steps[currentStep].inputId);
    if (currentStepInputNode) {
      currentStepInputNode.focus();
    }
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

  // On step button click, change the current step and reset the status of all steps after the clicked step
  const handleClickStep = (i: number) => {
    setHasWizardStepChanged(true);
    onStepChange(i);
  };

  const renderSummaryStep = () => (
    <Utility vAlignSelf="center" vFlex vFlexCol vGap={10} style={{ maxWidth: '610px', width: '100%' }}>
      <UtilityFragment vAlignSelf="center" vFlex vJustifyContent="center" vPadding={24} vGap={32}>
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
      <>
        <Utility vContainerHide="xs">
          <Utility vJustifyContent="between" vFlex vFlexWrap vGap={24}>
            <Utility>
              <Button onClick={handleSave} colorScheme="secondary">
                Save
              </Button>
            </Utility>
            <Utility vJustifyContent="end" vFlex vFlexWrap vGap={24}>
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
        <UtilityFragment vContainerHide="desktop">
          <Utility vFlex vFlexCol vGap={16} vContainerHide="sm">
            <Button onClick={handleSave} colorScheme="secondary">
              Save
            </Button>
            <Button onClick={handleClickPrevious} colorScheme="secondary">
              <VisaArrowBackTiny />
              Back
            </Button>
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
        </UtilityFragment>
      </>
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

  const renderDesktopWizard = () => {
    return (
      <nav aria-label={`${navRegionAriaLabel}-desktop`}>
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
    );
  };

  const renderMobileWizard = () => {
    return (
      <nav aria-label={`${navRegionAriaLabel}-mobile`}>
        <UtilityFragment vJustifyContent="center">
          <Wizard
            compact
            style={
              {
                '--v-wizard-compact-gap': 'clamp(var(--size-scalable-12), 6vw, var(--size-scalable-72))',
              } as CSSProperties
            }
          >
            {steps.map((step, i) => (
              <WizardStep key={`horizontal-wizard-step-${i + 1}`} aria-current={currentStep === i ? 'step' : undefined}>
                <ScreenReader>
                  {`${isStepError(i) ? 'Error ' : isStepComplete(i) ? 'Completed ' : ''}Step ${i + 1} of ${steps.length}`}
                </ScreenReader>
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
              </WizardStep>
            ))}
          </Wizard>
        </UtilityFragment>
      </nav>
    );
  };

  return (
    <Utility vFlex vFlexCol vGap={48} style={{ containerType: 'inline-size' } as CSSProperties}>
      <Utility vFlex vFlexCol vGap={16}>
        {showSavedFlag && (
          <Utility vAlignSelf="end">
            <Flag messageType="success">
              <FlagIcon />
              <FlagContent className="v-pl-2 v-pb-2" role="alert" aria-live="polite">
                <ScreenReader>success</ScreenReader>
                Your progress has been saved.
              </FlagContent>
              <FlagCloseButton onClick={() => setShowSavedFlag(false)} />
            </Flag>
          </Utility>
        )}
        <UtilityFragment vContainerHide="mobile">{renderDesktopWizard()}</UtilityFragment>
        <UtilityFragment vContainerHide="desktop">{renderMobileWizard()}</UtilityFragment>
        {steps.slice(0, steps.length - 1).map((step, i) => {
          return (
            <Utility key={i} vFlex vFlexCol vGap={24} vHide={currentStep !== i}>
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
              </Utility>
              {renderActionButtons()}
            </Utility>
          );
        })}
        {currentStep === steps.length - 1 && renderSummaryStep()}
      </Utility>
    </Utility>
  );
};

```

## Property Sections
### Wizard
- **Selector**: <Wizard />
- **Description**: Manages and navigates multi-step processes within your application.

### WizardStep
- **Selector**: <WizardStep />
- **Description**: Represents an individual step within a multi-step wizard process.

### Badge
- **Selector**: <Badge />
- **Description**: Visual indicators communicating the status of a component.

### Button
- **Selector**: <Button />
- **Description**: Interactive elements enabling users to take actions within an interface.

### useWizard
- **Selector**: None
- **Description**: This hook is used to control the state of a wizard component.

### badge
- **Selector**: <Badge />
- **Description**: 

### button
- **Selector**: <Button />
- **Description**: 

## Properties
### compact
- **Section**: Wizard
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: show wizard in compact

### ref
- **Section**: Wizard
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Wizard
- **Type**: ElementType
- **Default**: ol
- **Required**: false
- **Description**: Tag of Component

### vertical
- **Section**: Wizard
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: show wizard in vertical

### element
- **Section**: WizardStep
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### ref
- **Section**: WizardStep
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: WizardStep
- **Type**: ElementType
- **Default**: li
- **Required**: false
- **Description**: Tag (not compatible with element property)

### active
- **Section**: Badge
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Active style

### badgeType
- **Section**: Badge
- **Type**: "subtle" , "critical" , "neutral" , "stable" , "warning"
- **Default**: 
- **Required**: false
- **Description**: Type of Badge

### badgeVariant
- **Section**: Badge
- **Type**: "number" , "icon"
- **Default**: 
- **Required**: false
- **Description**: Variant of Badge

### clear
- **Section**: Badge
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Clear background

### ref
- **Section**: Badge
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Badge
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: Button
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: Button
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### element
- **Section**: Button
- **Type**: ReactElement
- **Default**: 
- **Required**: false
- **Description**: Cloned Element (not compatible with tag property)

### iconButton
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: Button
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: Button
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: Button
- **Type**: ElementType
- **Default**: button
- **Required**: false
- **Description**: Tag (not compatible with element property)

