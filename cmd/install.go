package cmd

import (
	"os"
	"os/exec"

	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

func installPackage(cats map[string]string) {
	color.Blue("Looking for cache...")
	if err := os.Mkdir(getTemporaryPath()+"core", os.ModePerm); err == nil {
		color.Red("Cache not found")
		color.Blue("Loading cache...")
		cmd := exec.Command("git", "clone", cats["core"], getTemporaryPath()+"core")
		cobra.CheckErr(cmd.Run())
		color.Green("Sucsessiful downloaded")
	}
}

// installCmd represents the install command
var installCmd = &cobra.Command{
	Use:   "install",
	Short: "install a package",
	Long:  ``,
	Args:  cobra.MinimumNArgs(1),
	Run: func(cmnd *cobra.Command, args []string) {
		cats := repos["bpak"]
		color.Blue("Looking for Git...")
		if _, err := exec.LookPath("git"); err == nil {
			color.Green("Git found!")
			installPackage(cats)
		}
	},
}

func init() {
	rootCmd.AddCommand(installCmd)
}
